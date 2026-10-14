from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    limite_credito = models.PositiveIntegerField(help_text="Cupo en CLP")

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    codigo_seguimiento = models.CharField(max_length=20, unique=True)
    fecha_pedido = models.DateField(auto_now_add=True)
    direccion_entrega = models.CharField(max_length=150)
    total = models.PositiveIntegerField(help_text="Total de la compra en CLP")

    def __str__(self):
        return f"Pedido {self.codigo_seguimiento} - {self.cliente.nombre}"