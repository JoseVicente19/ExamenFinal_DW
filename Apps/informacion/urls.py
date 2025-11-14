
from django.contrib import admin
from django.urls import path, include
from .views import InformacionView
from Apps.informacion import views

app_name = 'informacion'

urlpatterns = [
    path('', InformacionView.as_view(), name='infoapp'),
]
