from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView

from prices.models import StorePrice
from prices.forms import StorePriceForm



# Create your views here.
class StorePriceListView(ListView):
    model = StorePrice
    template_name = 'prices/price_list.html'
    context_object_name = 'prices'

class StorePriceCreateView(CreateView):
    model = StorePrice
    form_class = StorePriceForm
    template_name = 'prices/price_add_form.html'
    success_url = reverse_lazy('price_list')