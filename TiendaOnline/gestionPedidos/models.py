from django.db import models

# Create your models here.

class Clientes(models.Model):
    """Tabla clientes"""
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name= "La Direccion")
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return 'Nombre: {}'.format(self.nombre)


class Articulos(models.Model):
    """Tabla articulos"""
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'El nombre: {} - La seccion: {} - El precio: {}'.format(self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    """Tabla pedidos"""
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
