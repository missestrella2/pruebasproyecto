from django.db import models
#from ast import mod
#from email.policy import default
#from tabnanny import verbose
from django.db import models



class Cliente(models.Model):
    nombre= models.CharField(max_length=100, default=" ",verbose_name='Nombre')
    apellido= models.CharField(max_length=100, default=" ", verbose_name='Apellido')
    email= models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return f"{self.id} - {self.apellido}, {self.nombre}"

    def save(self, *args, **kwargs):
        if self.apellido.upper() == 'MESSI':
            raise ValueError("No se puede crear clientes con ese apellido")
        else:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.email.upper() == 'almada@gmail.com':
            raise ValueError("No se puede eliminar a Almada")
        return super().delete(*args, **kwargs)
    
    class Meta:
        db_table = 'Clientes'
        managed = True
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    