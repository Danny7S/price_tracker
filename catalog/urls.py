from django.urls import path
from .views import CategoryListView, CategoryCreateView, CategoryEditView, CategoryDeleteView, ProductListView, \
    ProductCreateView, ProductEditView, ProductDeleteView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/',CategoryEditView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/',CategoryDeleteView.as_view(), name='category_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/',ProductEditView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),

]