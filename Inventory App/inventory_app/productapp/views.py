from django.shortcuts import render
from productapp.models import product
from productapp.forms import productform
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
def list_products(request): # HTTPRequest  , web request
    products = product.objects.all() # ' select * from products'
    print(product)
    return render(request, 'productapp/index.html', {'productkeys' : products}  ) #HttpResponse  web Response

def product_detail(request, product_id):
    productdetail = get_object_or_404(product, pk=int(product_id))
    return render(request, 'productapp/detail.html', {'productdetail': productdetail})

def add_product(request):
    if request.method=='GET':
        return render(request, 'productapp/form.html',{'productform' : productform})
    else:
        form=productform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect(reverse('products:list_products'))
        else:
            return render(request, 'productapp/form.html', {'productform': productform})

def update_product(request,product_id):
    updatecontent = get_object_or_404(product,pk=int(product_id))
    if request.method=='GET':
        product_form = productform(instance=updatecontent)
        return render(request, 'productapp/update.html',{'productform':product_form})
    else:
        product_form = productform(request.POST,instance=updatecontent)
        if product_form.is_valid():
            product_form.save(commit=True)
            return HttpResponseRedirect(reverse('products:list_products'))
        else:
            return render(request, 'productapp/update.html',{'productform':product_form})

def delete_product(request, product_id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    instance = get_object_or_404(product, pk=product_id)

    if request.method == "POST":
        # delete object
        instance.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect(reverse('products:list_products'))

    return render(request, "productapp/deleteinstance.html", context)