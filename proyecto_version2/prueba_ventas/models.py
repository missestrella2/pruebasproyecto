from django.db import models
#from ast import mod
#from email.policy import default
#from tabnanny import verbose
from django.db import models


class Venta(models.Model):
    fecha_de_venta=models.DateField(verbose_name='Fecha de Venta')
    monto= models.CharField(max_length=100, default=" ", verbose_name='Monto')




