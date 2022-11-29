from django.urls import path, re_path
from . import views

urlpatterns=[

    path('pagoformas/listadepagoformas/',views.ListaDePagoFormas.as_view(),name='listadepagoformas'),
    path('pagoformas/altapagoformaform/',views.altapagoformaform.as_view(),name='altapagoformaform'),
    path('pagoformas/bajapagoformaform/',views.bajapagoformaform.as_view(),name="bajapagoformaform"),
    path('pagoformas/pagoformaeditar/<int:id_pagoforma>',views.pagoformaeditar,name='pagoformaeditar'),
    path('pagoformas/pagoformaeliminar/<int:id_pagoforma>',views.pagoformaeliminar,name='pagoformaeliminar'),
    path('pagoformas/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),
]