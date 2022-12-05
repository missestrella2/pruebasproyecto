from django.urls import path, re_path
from . import views

urlpatterns=[

    path('prueba_clientes/listadeclientes/',views.ListaDeClientes.as_view(),name='listadeclientes'),
    path('prueba_clientes/altaclienteform', views.AltaClienteForm.as_view(), name='AltaClienteForm'),
    path('prueba_clientes/bajaclienteform',views.BajaClienteForm.as_view(),name="BajaClienteForm"),
    path('prueba_clientes/clienteeditar/<int:id_cliente>',views.clienteeditar,name='clienteeditar'),
    path('prueba_clientes/clienteeliminar/<int:id_cliente>',views.clienteeliminar,name='clienteeliminar'),
    path('prueba_clientes/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),
]