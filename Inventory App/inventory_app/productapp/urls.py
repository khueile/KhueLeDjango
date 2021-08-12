from django.urls import path

from productapp.views import list_products, product_detail,add_product,update_product, delete_product

app_name='productapp'
urlpatterns=[
    path('',list_products.as_view(), name='list_products'),
    path('<int:pk>/', product_detail.as_view(), name='product_detail'),
    path('add/',add_product.as_view(),name='add_product'),
    path('<int:pk>/update/', update_product.as_view(), name='update_product'),
    path('<int:pk>/delete/', delete_product.as_view(), name='delete_product'),
]