from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class Servicio(models.Model):
    tipo_de_servicio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio_base = models.BigIntegerField()

    def __str__(self):
        return self.tipo_de_servicio

class Paquete(models.Model):
    nombre_paquete = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.BigIntegerField()

    def __str__(self):
        return self.nombre_paquete

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    telefono = models.BigIntegerField()
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Reserva(models.Model):
    fecha_reserva = models.DateTimeField()
    estado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    def __str__(self):
        return f"Reserva {self.id} - {self.cliente}"

class Venta(models.Model):
    fecha_venta = models.DateTimeField()
    total = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    paquete = models.ForeignKey(Paquete, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"

class Foto(models.Model):
    url = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=50)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return self.url

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Cambia el related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # Cambia el related_name
        blank=True,
    )

# Create your models here.
