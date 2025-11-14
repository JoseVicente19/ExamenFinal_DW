from django.shortcuts import render
from django.views.generic import TemplateView


class InformacionView(TemplateView):
    template_name = 'informacion.html'