from django.urls import path

from .views import StoreListView,StoreCreateView,StoreDeleteView,StoreUpdateView

urlpatterns = [
    path('stores/', StoreListView.as_view(), name='store_list'),
    path('stores/add/', StoreCreateView.as_view(), name='store_create'),
    path('stores/<int:pk>/edit/', StoreUpdateView.as_view(), name='store_edit'),
    path('stores/<int:pk>/delete/', StoreDeleteView.as_view(), name='store_delete'),
]