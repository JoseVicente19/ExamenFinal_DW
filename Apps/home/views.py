from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Usuario
from django.urls import reverse_lazy
from .forms import RegistroForm
from django.contrib.auth.views import LoginView

# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class RegistroView(CreateView):
    model = Usuario
    form_class = RegistroForm
    success_url = reverse_lazy('home:homeapp')

class LoginView(LoginView):
    template_name = 'login.html'