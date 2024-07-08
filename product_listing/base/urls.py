from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/shop/<int:fk>/', views.ProductListFromShopIDView.as_view(), name='product-shop'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:id>/', views.ProductView.as_view(), name='product-view'),
    path('category/', views.CategoryListView.as_view(), name='category-create'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-list'),
    path('region/', views.RegionListView.as_view(), name='region-list'),
    path('region/create/', views.RegionCreateView.as_view(), name='region-create'),

] 