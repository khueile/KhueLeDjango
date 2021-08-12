from django.shortcuts import render
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

class add_product(CreateView):
    model=product
    template_name='productapp/form.html'
    form_class=productform
    #context_object_name='productform'
    #fields = ['name', 'description', 'count', 'location']
    success_url=reverse_lazy('productapp:list_products')

class update_product(UpdateView):
    model=product
    template_name = 'productapp/update.html'
    form_class = productform
    #productform(request.POST).save(commit=True)
    success_url = reverse_lazy('productapp:list_products')


class delete_product(DeleteView):
    model = product
    template_name = 'productapp/deleteinstance.html'
    success_url = reverse_lazy('productapp:list_products')



