from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from productapp.models import product
from productapp.forms import productform
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View, CreateView,UpdateView,DeleteView

# Create your views here.
class list_products(ListView): # HTTPRequest  , web request
    model=product
    template_name= 'productapp/index.html'
    context_object_name='productkeys'

class product_detail(DetailView):
    model=product
    template_name= 'productapp/detail.html'
    #context_object_name='productdetail'

class add_product(LoginRequiredMixin,CreateView):
    model=product
    template_name='productapp/form.html'
    form_class=productform
    #context_object_name='productform'
    #fields = ['name', 'description', 'count', 'location']
    success_url=reverse_lazy('productapp:list_products')

    login_url = 'login'# appname:viewname accounts/login

    def form_valid(self, form): #MRO
        form.instance.user = self.request.user # logged in user
        return super(RestaurantCreate, self).form_valid(form)


class update_product(LoginRequiredMixin,UpdateView):
    model=product
    template_name = 'productapp/update.html'
    form_class = productform
    #productform(request.POST).save(commit=True)
    success_url = reverse_lazy('productapp:list_products')

    login_url = 'login'# appname:viewname accounts/login

    def form_valid(self, form): #MRO
        form.instance.user = self.request.user # logged in user
        return super(RestaurantCreate, self).form_valid(form)


class delete_product(DeleteView):
    model = product
    template_name = 'productapp/deleteinstance.html'
    success_url = reverse_lazy('productapp:list_products')



