from django import forms
from .models import Category, Product

allowed_slug_caracters="-1234567890"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','slug']

        labels = {
            'name': 'Category Name',
            'description': 'Category Description',
            'slug': 'Category Slug',
        }

        help_texts = {
            'slug': 'Use lowercase letters, numbers and hyphens only.',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter category description',
                'rows': 3,
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. dairy-products',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name.strip()) < 3:
            raise forms.ValidationError(
                "Category name must be at least 3 characters long."
            )

        return name

    def clean_description(self):
        description = self.cleaned_data['description']

        if len(description.strip()) > 300:
            raise forms.ValidationError(
                "Category description must not exceed 300 characters."
            )
        return description


    def clean_slug(self):
        slug = self.cleaned_data['slug']
        correct_slug = 0
        if not (all(el in allowed_slug_caracters for el in slug) or slug.islower()):
            raise forms.ValidationError(
                "Category slug can only be lowecase letters , numbers , and hyphens."
            )
        if len(slug)<3:
            raise forms.ValidationError(
                "Category slug must be at least 3 characters long."
            )
        return slug



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','brand','description','category','image']

        labels = {
            'name': 'Product Name',
            'brand': 'Brand',
            'description': 'Product Description',
            'category': 'Category',
            'image': 'Product Image',
        }

        help_texts = {
            'image': 'Upload an image of the product (optional).',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name',
            }),
            'brand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter brand name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product description',
                'rows': 3,
            }),
            'category': forms.Select(attrs={
                'class': 'form-select',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 3:
            raise forms.ValidationError(
                "Product name must be at least 3 characters long."
            )

        return name

    def clean_brand(self):
        brand = self.cleaned_data['brand']

        if len(brand) > 30:
            raise forms.ValidationError(
                "Product brand must be less than 30 characters long."
            )
        return brand

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 300:
            raise forms.ValidationError(
                "Product description must not exceed 300 characters."
            )

        return description
