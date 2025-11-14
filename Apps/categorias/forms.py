from django import forms
from .models import Categoria

class CatForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'