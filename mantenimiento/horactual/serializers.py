from rest_framework import serializers
from horactual.models import FechaHora
  # Mario Rojas: Serializar la instancia FechaHora del modelo para ser transmitidas en formato JSON
class FechaHoraSerializer(serializers.ModelSerializer):
	class Meta:
		model = FechaHora #Clase a serializar
		fields = ('hora_actual', ) #Campo a serializar
