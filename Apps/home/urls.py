
from django.contrib import admin
from django.urls import path
from .views import HomeView, RegistroView, LoginView
from Apps.home import views

app_name='home'
urlpatterns = [
    path('', HomeView.as_view(), name='homeapp'),
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),

]
