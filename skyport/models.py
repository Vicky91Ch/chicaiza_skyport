from django.db import models

class Aerolinea(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=120)

    def __str__(self):
        return self.codigo

class Vuelo(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    destino = models.CharField(max_length=100, unique=True)
    duracion_minutos = models.TimeField(null=True, blank=True) 
    precio = models.DecimalField(
        max_digits=10,  # total de dígitos
        decimal_places=2,  # decimales
        default=0
    )
    activo = models.BooleanField(default=True)
    Aerolinea = models.ForeignKey(Aerolinea, on_delete=models.PROTECT, related_name="vuelos")


    def __str__(self):
        return f"{self.aerolinea.codigo} {self.codigo}"