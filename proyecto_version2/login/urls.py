from django.conf import settings
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[

    path('',views.index,name="index"), 
    path('indexform/',views.indexform,name="indexform"), 
    path('paginaenblanco2/',views.paginaenblanco2,name="paginaenblanco2"),

    path('logout/',auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'), 
]