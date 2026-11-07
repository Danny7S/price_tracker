from django import forms

from prices.models import StorePrice

class StorePriceForm(forms.ModelForm):

    class Meta:
        model = StorePrice
        fields = ['product', 'store', 'price','note']
