from datetime import date
from django.db import models


class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    telefono = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to="foto_perfil", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    fecha_inicio = models.DateField(("Date"), default=date.today)
    fecha_fin = models.DateField(("Date"), default=date.today)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE, default="")
    prioridad_tarea_choices = (
        ('Urgente', 'Urgente'),
        ('Alta', 'Alta'),
        ('Moderada', 'Moderada'),
        ('Baja', 'Baja'),
    )
    nivel_prioridad = models.CharField(choices=prioridad_tarea_choices, default='', max_length=20)
    notas = models.TextField(max_length=300)
    estado_tarea_choices = (
        ('Abierta', 'Abierta'),
        ('Asignada', 'Asignada'),
        ('En proceso', 'En proceso'),
        ('Finalizada', 'Finalizada'),
    )
    estado_tarea = models.CharField(choices=estado_tarea_choices, default='', max_length=20)

    def __str__(self):
        return f"{self.nombre}"


class Proyecto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    fecha_inicio = models.DateField(("Date"), default=date.today)
    fecha_fin = models.DateField(("Date"), default=date.today)
    presupuesto = models.IntegerField(default=0)
    nombre_cliente = models.CharField(max_length=20, default="")
    apellidos_cliente = models.CharField(max_length=50, default="")
    email_cliente = models.EmailField(max_length=100, default="")
    telefono_cliente = models.IntegerField(default=0)
    tarea = models.ManyToManyField(Tarea)
    responsable = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.id}"
