from django.urls import path #segun clase 10
from . import views #segun clase 10 significa: desde donde estoy importa las vistas

urlpatterns=[

    path('historial-ventas/',views.historial_ventas,name="historial_ventas"),
    path('historial-ventas/histventform',views.histventform,name="histventform"),
]