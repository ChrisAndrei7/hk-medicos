from rest_framework import serializers
from entities.pedidos.pedidosmodels import Pedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'