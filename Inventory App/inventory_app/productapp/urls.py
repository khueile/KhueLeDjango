from django.urls import path

from productapp.views import list_products, product_detail,add_product,update_product,delete_product

app_name='productapp'
urlpatterns=[
    path('',list_products, name='list_products'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('add/',add_product,name='add_product'),
    path('<int:product_id>/update/', update_product, name='update_product'),
    path('<int:product_id>/delete/', delete_product, name='delete_product'),
]