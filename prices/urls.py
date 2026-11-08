from django.urls import path
from .views import StorePriceListView, StorePriceCreateView,StorePriceEditView,StorePriceDeleteView


urlpatterns = [
    path('prices/', StorePriceListView.as_view(), name='price_list'),
    path('prices/add/', StorePriceCreateView.as_view(), name='price_create'),
    path('prices/<int:pk>/edit/', StorePriceEditView.as_view(), name='price_edit'),
    path('prices/<int:pk>/delete/', StorePriceDeleteView.as_view(), name='price_delete'),
]