from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    # Relación simple entre modelos [cite: 122]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')])
    fecha = models.DateTimeField(auto_now_add=True)