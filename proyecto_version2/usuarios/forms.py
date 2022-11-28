from django import forms
from django.forms import ValidationError
from .models import Usuario
#from .models import Cargo

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class AltaUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class BajaUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email','password']

class BuscarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre']