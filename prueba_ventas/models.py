from django.db import models
#from ast import mod
#from email.policy import default
#from tabnanny import verbose
from django.db import models
from pagoformas.models import PagoForma
from prueba_clientes.models import Cliente

class Venta(models.Model):
    clientes = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    pagoformas = models.ManyToManyField(PagoForma, through='PagoForma')
    fecha_de_venta=models.DateField(verbose_name='Fecha de Venta')
    monto= models.IntegerField(default=0,verbose_name='Monto')
    
    class Meta:
        db_table = 'Ventas'
        managed = True
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
