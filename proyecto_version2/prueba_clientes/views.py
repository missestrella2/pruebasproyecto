from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from prueba_clientes.forms import ClientesForm, AltaClienteForm, BajaClienteForm
from django.contrib import messages
from prueba_clientes.models import Cliente
from django.views import View
from django.views.generic import ListView


def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'prueba_clientes/paginaenblanco.html', {"context": context})

class ListaDeClientes(ListView):
    model = Cliente 
    context_object_name = 'clientes'
    template_name = 'prueba_clientes/listadeclientes.html'
    ordering =['id']

def clienteeditar(request, id_cliente): #BOTON EDITAR EN LISTADO
    try:
        cliente = Cliente.objects.get(id=id_cliente)
    except Cliente.DoesNotExist:
        return render(request, 'prueba_clientes/404.html')
    
    if request.method == "POST":
        formulario = ClientesForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadeclientes')
    else:
        formulario = ClientesForm(instance=cliente)

    return render(request, 'prueba_clientes/clienteeditar.html', {'formulario': formulario, 'id_cliente': id_cliente})


def clienteeliminar(request, id_cliente): #BOTON ELIMINAR EN LISTADO 
    try:
        cliente = Cliente.objects.get(id=id_cliente)
    except Cliente.DoesNotExist:
        return render(request, 'prueba_clientes/404.html')
    
    try:
        cliente.delete()
    except ValueError as ve:
        messages.error(request=request, message="no se puede borrar")
    return redirect('listadeclientes')

class altaclienteform(View): #FORMULARIO DE ALTA
    form_class = AltaClienteForm
    template_name = 'prueba_clientes/altaclienteform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeclientes')

        return render(request, self.template_name, {'formulario': form})

class bajaclienteform(View): #FORMULARIO DE BAJA
    form_class = BajaClienteForm
    template_name = 'prueba_clientes/bajaclienteform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        try:
            cliente_a_borrar= Cliente.objects.get(email=email,password=password)
        except Cliente.DoesNotExist:
            return render(request, "prueba_clientes/404.html")    
        try:    
            cliente_a_borrar.delete()
        except ValueError as ve:
            bajaclienteform.add_error('email', str(ve))
        else:
            return redirect('listadeclientes')

        return render(request, self.template_name, {'formulario': form})

