from django.shortcuts import render
from .models import *
from .serializers import *

from django.db.models import Q

from rest_framework import generics, permissions

from django.shortcuts import get_object_or_404

# Create your views here.

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class ProductListFromShopIDView(generics.ListAPIView):
    serializer_class = ProductSerializer
    http_method_names = ['get']

    def get_queryset(self):
        fk = self.kwargs.get('fk')
        shop = get_object_or_404(Shop, pk=fk)
        products = Product.objects.filter(shop_id=shop)
        return products

class ProductView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    http_method_names = ['get']


class RegionCreateView(generics.CreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    http_method_names = ['get']



class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['post']

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']

