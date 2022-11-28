from django.urls import path, re_path
from . import views

urlpatterns=[

    path('prueba_ventas/listadeventas/',views.ListaDeVentas.as_view(),name='listadeventas'),
    path('prueba_ventas/altaventaform', views.altaventaform.as_view(), name='altaventaform'),
   # path('prueba_ventas/bajaventaform',views.bajaventaform.as_view(),name="bajaventaform"),
   # path('prueba_ventas/ventaeditar/<int:id_venta>',views.ventaeditar,name='ventaeditar'),
   # path('prueba_ventas/ventaeliminar/<int:id_venta>',views.ventaeliminar,name='ventaeliminar'),
    path('prueba_ventas/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),

    path('prueba_ventas/buscarventas/',views.buscarventas,name='buscarventas'),
    
]