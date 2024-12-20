from django.shortcuts import render, redirect
from .forms import CategoryForm, ProductForm, CustomerForm, SearchForm
from .models import Category, Product, Customer

# Vista de inicio
def home(request):
    return render(request, 'myapp/home.html')

# Vista para agregar categoría
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CategoryForm()
    return render(request, 'myapp/add_category.html', {'form': form})

# Vista para agregar producto
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = ProductForm()
    return render(request, 'myapp/add_product.html', {'form': form})

# Vista para agregar cliente
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = CustomerForm()
    return render(request, 'myapp/add_customer.html', {'form': form})

# Vista para buscar productos
def search(request):
    results = None
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            results = Product.objects.filter(name__icontains=query)
    else:
        form = SearchForm()

    return render(request, 'myapp/search.html', {'form': form, 'results': results})
