from django import forms

from prices.models import StorePrice

class StorePriceForm(forms.ModelForm):

    class Meta:
        model = StorePrice
        fields = ['product', 'store', 'price','note']

        labels = {
            'product': 'Product',
            'store': 'Store',
            'price': 'Price (EUR)',
            'note': 'Additional Notes',
        }

        help_texts = {
            'price': 'Enter the current price of the product in EUR.',
        }

        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-select',
            }),
            'store': forms.Select(attrs={
                'class': 'form-select',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price',
                'step': '0.01',
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Optional notes',
                'rows': 3,
            }),
        }

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError(
                "Price must be greater than zero."
            )

        if price > 100000:
            raise forms.ValidationError(
                "Price cannot exceed 100000."
            )

        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['product'].disabled = True