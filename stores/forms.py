from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'description']

        labels = {
            'name': 'Store Name',
            'address': 'Store Address',
            'description': 'Store Description',
        }

        help_texts = {
            'address': 'Enter the physical address of the store.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter store name',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter store address',
                'rows': 2,
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter store description',
                'rows': 3,
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError(
                "Store name must be at least 3 characters long."
            )

        return name

    def clean_address(self):
        address = self.cleaned_data['address']

        if len(address) > 200:
            raise forms.ValidationError(
                "Store address cannot exceed 200 characters."
            )

        return address

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description) < 300:
            raise forms.ValidationError(
                "Store description must not exceed 300 characters."
            )

        return description