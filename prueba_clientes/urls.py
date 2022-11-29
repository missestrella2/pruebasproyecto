from django.urls import path, re_path
from . import views

urlpatterns=[

    path('prueba_clientes/listadeclientes/',views.ListaDeClientes.as_view(),name='listadeclientes'),
    path('prueba_clientes/altaclienteform', views.altaclienteform.as_view(), name='altaclienteform'),
    path('prueba_clientes/bajaclienteform',views.bajaclienteform.as_view(),name="bajaclienteform"),
    path('prueba_clientes/clienteeditar/<int:id_cliente>',views.clienteeditar,name='clienteeditar'),
    path('prueba_clientes/clienteeliminar/<int:id_cliente>',views.clienteeliminar,name='clienteeliminar'),
    path('prueba_clientes/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),
]