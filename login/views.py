from datetime import datetime

from datetime import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from django.views.generic import ListView
from login.forms import IndexForm


def index(request):
    return redirect('login')

def logout_view(request):
     logout(request)
     return redirect('logout')


def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'login/paginaenblanco.html', {"context": context})