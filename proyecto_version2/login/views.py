from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse  # segun la clase de forms
#from django.shortcuts import render  # segun la clase de forms
from django.urls import reverse
from django.template import loader
from .forms import IndexForm  # segun la clase de forms

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
#from login.models import 
#from django.views import View
#from django.views.generic import ListView
from login.forms import IndexForm


def index(request):
    context = {"hoy": datetime.now}
    marca = 'Pig Crm'

    return render(request, 'login/index.html', {"marca": marca, "context": context})

def indexform(request):
    if request.method == 'POST':
        indexform = IndexForm(request.POST)
        # if login_form.is_valid():
        #     messages.info(request, "Info importante")
    else:
        indexform =IndexForm()
    return render(request, 'login/indexform.html', {'indexform': indexform})

def paginaenblanco2(request):
    context = {"hoy": datetime.now}
    return render(request, 'login/paginaenblanco2.html', {"context": context})

def index(request):  ########### PAGINA DE LOGIN !!! #################
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            # messages.success(request, f' Bienvenido/a {username} !!')
            return redirect('paginaenblanco2')
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    
    form = AuthenticationForm()
    return render(request, 'login/index.html', {'form': form, 'title': 'Log in'})

def logout_view(request):
     logout(request)
     return redirect('index')