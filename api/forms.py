from django import forms
from .model.product_model import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'productTitle', 'product_type', 'description', 'image', 'bestSeller']
