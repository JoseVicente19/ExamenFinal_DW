from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from .models import Estudiante
from django.urls import reverse_lazy
from .forms import EstudianteForm

class EstuView(ListView): 
    model = Estudiante
    template_name = 'estudiantes.html'
    context_object_name = 'lista_estudiantes'

    def get_queryset(self):
        vNombre = self.request.GET.get('NOMBRE')
        if(vNombre):
            return Estudiante.objects.filter(nombre__icontains=vNombre)
        else:
            return Estudiante.objects.all()


class CrearEstudianteView(CreateView):
    template_name = 'crear.html'
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes:estuapp')


class EditarEstudianteView(UpdateView):
    template_name = 'editar.html'
    model = Estudiante
    form_class = EstudianteForm
    success_url = reverse_lazy('estudiantes:estuapp')