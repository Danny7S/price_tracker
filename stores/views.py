from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Store
from .forms import StoreForm

class StoreListView(ListView):
    model = Store
    template_name = 'stores/store_list.html'
    context_object_name = 'stores'

class StoreCreateView(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'stores/store_add_form.html'
    success_url = reverse_lazy('store_list')



