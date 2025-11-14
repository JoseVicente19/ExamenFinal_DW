"""
URL configuration for ColegioA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Apps.estudiantes import views
from .views import CategoriaView, CrearCatView, EditarCatView

app_name='categoria'
urlpatterns = [
    path('', CategoriaView.as_view(), name='categoria'),
    path('crear/', CrearCatView.as_view(), name='crearcat'),
    path('editar/ <int:pk>', EditarCatView.as_view(), name='editarcat'),
    #path('ver/ <int:pk>', VerDetailView.as_view(), name='ver'),

]