from rest_framework import serializers
from myCarW.models import Insumos

# creamos la clase que permite serializar el modelo

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumos
        fields = ["nombre","precio","descripcion","stock"] # "__all__"

