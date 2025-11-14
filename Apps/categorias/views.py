from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import Categoria
from django.urls import reverse_lazy
from .forms import CatForm
# Create your views here.

class CategoriaView(ListView): 
    model = Categoria
    template_name = 'categorias.html'
    context_object_name = 'lista_categorias'



class CrearCatView(CreateView):
    template_name = 'crearcat.html'
    form_class = CatForm
    success_url = reverse_lazy('categoria:categoria')


class EditarCatView(UpdateView):
    template_name = 'editarcat.html'
    model = Categoria
    form_class = CatForm
    success_url = reverse_lazy('categoria:categoria')
