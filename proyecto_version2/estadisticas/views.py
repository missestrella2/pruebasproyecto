
from django.shortcuts import render 
from django.template import loader 
from django.http import HttpResponse 
from datetime import datetime 

# Create your views here.

from django.http import HttpResponse 

def estadisticas(request):                                                #asi se cargan los templates
    template = loader.get_template('estadisticas/estadisticas.html')   #crea objeto template que trae a index.html
    context = {"hoy":datetime.now}                                 #creo context que es un diccionario
    return HttpResponse(template.render(context,request))

