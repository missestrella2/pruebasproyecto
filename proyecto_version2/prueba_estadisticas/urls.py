from django.urls import path, re_path
from . import views

urlpatterns=[
    path('prueba_estadisticas/paginaenblanco/',views.paginaenblanco2,name='paginaenblanco2'),
]