from django.contrib import admin
from .models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'email', 'formato_limite')
    list_filter = ('nombre',)
    search_fields = ('rut', 'nombre', 'email')

    @admin.display(description='Límite Crédito')
    def formato_limite(self, obj):
        return f"${obj.limite_credito:,.0f}".replace(",", ".")

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo_seguimiento', 'cliente', 'fecha_pedido', 'formato_total')
    list_filter = ('fecha_pedido', 'cliente')
    search_fields = ('codigo_seguimiento', 'cliente__nombre')

    @admin.display(description='Total')
    def formato_total(self, obj):
        return f"${obj.total:,.0f}".replace(",", ".")