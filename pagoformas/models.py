from django.db import models
#from ast import mod
#from email.policy import default
#from tabnanny import verbose
from django.db import models

class PagoForma(models.Model):
    nombre= models.CharField(max_length=100, default=" ", verbose_name='Forma de Pago')
    
    def __str__(self):
        return f"{self.nombre}"

    def save(self, *args, **kwargs):
        if self.nombre.upper() == 'MESSI':
            raise ValueError("No se puede crear")
        else:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.nombre.upper() == 'Efectivo':
            raise ValueError("No se puede eliminar")
        return super().delete(*args, **kwargs)