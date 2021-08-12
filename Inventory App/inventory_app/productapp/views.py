from django.shortcuts import render
from productapp.models import product
from productapp.forms import productform
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View

# Create your views here.
class list_products(ListView): # HTTPRequest  , web request
    model=product
    template_name= 'productapp/index.html'
    context_object_name='productkeys'

class product_detail(DetailView):
    model=product
    template_name= 'productapp/detail.html'
    #context_object_name='productdetail'

class add_product(View):
    def get(self, request):
        return render(request, 'productapp/form.html',{'productform' : productform})
    def post(self, request):
        form=productform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('products:list_products'))
        else:
            return render(request, 'productapp/form.html', {'productform': productform})

class update_product(View):
    def get(self,request,**kwargs):
        print(request)
        #updatecontent = get_object_or_404(product, pk=int(product_id))
        updatecontent = get_object_or_404(product,pk=kwargs['pk'])
        product_form = productform(instance=updatecontent)
        return render(request, 'productapp/update.html',{'productform':product_form})
    def post(self,request):
        product_form = productform(request.POST,instance=updatecontent)
        if product_form.is_valid():
            product_form.save(commit=True)
            return HttpResponseRedirect(reverse('products:list_products'))
        else:
            return render(request, 'productapp/update.html',{'productform':product_form})



class delete_product(View):
    def get(self,request,**kwargs):
        context = {}
        instance = get_object_or_404(product, pk=kwargs['pk'])
        return render(request, "productapp/deleteinstance.html", context)

    def post(self, request,**kwargs):
        # dictionary for initial data with
        # field names as keys
        context = {}

        # fetch the object related to passed id
        instance = get_object_or_404(product, pk=kwargs['pk'])
        instance.delete()
        # after deleting redirect to

        # home page
        return HttpResponseRedirect(reverse('products:list_products'))



