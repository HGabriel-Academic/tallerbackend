from django.contrib import admin
from .models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'email', 'limite_credito')
    list_filter = ('nombre',)
    search_fields = ('rut', 'nombre', 'email')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo_seguimiento', 'cliente', 'fecha_pedido', 'total')
    list_filter = ('fecha_pedido', 'cliente')
    search_fields = ('codigo_seguimiento', 'cliente__nombre')
