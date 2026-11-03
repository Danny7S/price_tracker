from django.urls import path

from .views import StoreListView,StoreCreateView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store_list'),
    path('stores/add/', StoreCreateView.as_view(), name='store_create'),
]