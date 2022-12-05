from django import forms
from django.forms import ValidationError
from .models import Cliente

#from .models import Cargo

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class AltaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class BajaClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'