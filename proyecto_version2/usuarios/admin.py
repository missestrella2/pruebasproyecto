from django.contrib import admin
from usuarios.models import Usuario


class UsuariosAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido")


admin.site.register(Usuario,UsuariosAdmin)

