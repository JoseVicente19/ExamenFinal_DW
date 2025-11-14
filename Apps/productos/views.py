from django.views.generic import ListView, CreateView, UpdateView
from .forms import ProductoForm
from django.urls import reverse_lazy
from .models import Producto

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos_lista.html'
    context_object_name = 'lista_productos'

class CrearProdView(CreateView):
    template_name = 'crearprod.html'
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto')

class EditarProdView(UpdateView):
    template_name = 'editarprod.html'
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy('producto:producto')

