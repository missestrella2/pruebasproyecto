from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from usuarios.forms import UsuariosForm, AltaUsuarioForm, BajaUsuarioForm
from django.contrib import messages
from usuarios.models import Usuario
from django.views import View
from django.views.generic import ListView


def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'usuarios/paginaenblanco.html', {"context": context})

class ListaDeUsuarios(ListView):
    model = Usuario 
    context_object_name = 'usuarios'
    template_name = 'usuarios/listadeusuarios.html'
    ordering =['id']

def usuarioeditar(request, id_usuario): #BOTON EDITAR EN LISTADO
    try:
        usuario = Usuario.objects.get(id=id_usuario)
    except Usuario.DoesNotExist:
        return render(request, 'usuarios/404.html')
    
    if request.method == "POST":
        formulario = UsuariosForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadeusuarios')
    else:
        formulario = UsuariosForm(instance=usuario)

    return render(request, 'usuarios/usuarioeditar.html', {'formulario': formulario, 'id_usuario': id_usuario})


def usuarioeliminar(request, id_usuario): #BOTON ELIMINAR EN LISTADO 
    try:
        usuario = Usuario.objects.get(id=id_usuario)
    except Usuario.DoesNotExist:
        return render(request, 'usuarios/404.html')
    
    try:
        usuario.delete()
    except ValueError as ve:
        messages.error(request=request, message="no se puede borrar")
    return redirect('listadeusuarios')

class altausuarioform(View): #FORMULARIO DE ALTA
    form_class = AltaUsuarioForm
    template_name = 'usuarios/altausuarioform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeusuarios')

        return render(request, self.template_name, {'formulario': form})

class bajausuarioform(View): #FORMULARIO DE BAJA
    form_class = BajaUsuarioForm
    template_name = 'usuarios/bajausuarioform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        try:
            usuario_a_borrar= Usuario.objects.get(email=email,password=password)
        except Usuario.DoesNotExist:
            return render(request, "usuarios/404.html")    
        try:    
            usuario_a_borrar.delete()
        except ValueError as ve:
            bajausuarioform.add_error('email', str(ve))
        else:
            return redirect('listadeusuarios')

        return render(request, self.template_name, {'formulario': form})

