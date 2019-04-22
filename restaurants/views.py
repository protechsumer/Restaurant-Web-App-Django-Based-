from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView,CreateView, UpdateView
from django.db.models import Q
from .models import RestaurantLocation
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
# Create your views here.

@login_required(login_url='/login/')
def restaurant_createview(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    #title       = request.POST.get("title")
    #location    = request.POST.get("location")
    #category    = request.POST.get("category")
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            #obj = RestaurantLocation.objects.create(
            #   name        = form.cleaned_data.get('name'),
             #  location    = form.cleaned_data.get('location'),
            # category    = form.cleaned_data.get('category'))
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form.html'
    context  = {"form": form, "errors": errors}
    return render(request,template_name,context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {"object_list":queryset}
    return render(request,template_name,context)

def restaurant_detailview(request, slug):
    template_name = 'restaurants/restaurantlocation_detail.html'
    obj = RestaurantLocation.objects.get(slug=slug)
    context = {"object_list":obj}
    return render(request,template_name,context)

class RestaurantListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)

class RestaurantDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
      #  instance.save()
        return super(RestaurantCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context= super(RestaurantCreateView,self).get_context_data(*args, **kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'
    success_url = '/restaurants/'

    def get_context_data(self, *args, **kwargs):
        context= super(RestaurantCreateView,self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title'] = f'Update Restaurant: {name}'
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)