from django.urls import path
from .views import StorePriceListView, StorePriceCreateView


urlpatterns = [
    path('prices/', StorePriceListView.as_view(), name='price_list'),
    path('prices/add/', StorePriceCreateView.as_view(), name='price_create'),
]