from django import forms
from .models import Category, Product, Customer

# Formulario para agregar categoría
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

# Formulario para agregar producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price']

# Formulario para agregar cliente
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

# Formulario de búsqueda de productos
class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search Products', max_length=100)
