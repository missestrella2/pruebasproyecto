from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from prueba_ventas.forms import VentasForm, AltaVentaForm
from django.contrib import messages
from prueba_ventas.models import Venta
from django.views import View
from django.views.generic import ListView


def paginaenblanco2(request):
    context = {"hoy": datetime.now}
    return render(request, 'prueba_estadisticas/paginaenblanco2.html', {"context": context})
