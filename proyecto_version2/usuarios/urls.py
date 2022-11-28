from django.urls import path, re_path
from . import views

urlpatterns=[

    path('usuarios/listadeusuarios/',views.ListaDeUsuarios.as_view(),name='listadeusuarios'),
    path('usuarios/altausuarioform', views.altausuarioform.as_view(), name='altausuarioform'),
    path('usuarios/bajausuarioform',views.bajausuarioform.as_view(),name="bajausuarioform"),
    path('usuarios/usuarioeditar/<int:id_usuario>',views.usuarioeditar,name='usuarioeditar'),
    path('usuarios/usuarioeliminar/<int:id_usuario>',views.usuarioeliminar,name='usuarioeliminar'),
    path('usuarios/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),

    path('usuarios/buscarusuario/',views.buscarusuario,name='buscarusuario'),
]

