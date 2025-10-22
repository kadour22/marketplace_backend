from django.urls import path
from . import views

urlpatterns = [
    path('products-list/', views.product_list.as_view(),name='product-list'),
]
