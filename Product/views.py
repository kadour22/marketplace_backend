# rest imports 
from rest_framework import generics , status
from rest_framework.views import APIView
# local imports
from .serializers import product_serializer
from .models import Product
# django imports
from django.shortcuts import get_object_or_404


class product_list(generics.ListAPIView) :
    serializer_class = product_serializer
    queryset = Product.objects.select_related("seller").all()