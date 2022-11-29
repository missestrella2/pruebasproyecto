from django import forms
from django.forms import ValidationError
from .models import Venta
#from .models import Cargo

class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class AltaVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class BuscarVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('fecha_de_venta',)