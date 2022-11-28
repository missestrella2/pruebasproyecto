from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from pagoformas.forms import PagoFormasForm, AltaPagoFormaForm, BajaPagoFormaForm
from django.contrib import messages
from pagoformas.models import PagoForma
from django.views import View
from django.views.generic import ListView


def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'PagoFormas/paginaenblanco.html', {"context": context})

class ListaDePagoFormas(ListView):
    model = PagoForma 
    context_object_name = 'pagoformas'
    template_name = 'PagoFormas/listadepagoformas.html'
    ordering =['id']

def pagoformaeditar(request, id_pagoforma): #BOTON EDITAR EN LISTADO
    try:
        pagoforma = PagoForma.objects.get(id=id_pagoforma)
    except PagoForma.DoesNotExist:
        return render(request, 'pagoformas/404.html')
    
    if request.method == "POST":
        formulario = PagoFormasForm(request.POST, instance=pagoforma)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadepagoformas')
    else:
        formulario = PagoFormasForm(instance=pagoforma)

    return render(request, 'pagoformas/pagoformaeditar.html', {'formulario': formulario, 'id_pagoforma': id_pagoforma})


def pagoformaeliminar(request, id_pagoforma): #BOTON ELIMINAR EN LISTADO 
    try:
        pagoforma = PagoForma.objects.get(id=id_pagoforma)
    except PagoForma.DoesNotExist:
        return render(request, 'PagoFormas/404.html')
    
    try:
        pagoforma.delete()
    except ValueError as ve:
        messages.error(request=request, message="no se puede borrar")
    return redirect('listadepagoformas')

class altapagoformaform(View): #FORMULARIO DE ALTA
    form_class = AltaPagoFormaForm
    template_name = 'PagoFormas/altaPagoFormaform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadepagoformas')

        return render(request, self.template_name, {'formulario': form})

class bajapagoformaform(View): #FORMULARIO DE BAJA
    form_class = BajaPagoFormaForm
    template_name = 'PagoFormas/bajaPagoFormaform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            
        try:
            PagoForma_a_borrar= PagoForma.objects.get(nombre=nombre)
        except PagoForma.DoesNotExist:
            return render(request, "PagoFormas/404.html")    
        try:    
            PagoForma_a_borrar.delete()
        except ValueError as ve:
            bajaPagoFormaform.add_error('nombre', str(ve))
        else:
            return redirect('listadepagoformas')

        return render(request, self.template_name, {'formulario': form})