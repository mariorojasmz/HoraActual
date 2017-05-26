from django.shortcuts import render  
from rest_framework.response import Response
from rest_framework import viewsets 
from horactual.serializers import FechaHoraSerializer 
from horactual.models import FechaHora

import datetime

 # Mario Rojas: Definimos la clase FechaHoraViewSet heredando de ViewSet
class FechaHoraViewSet(viewsets.ViewSet):
     # ReEscribimos retrieve para almacenar el valor de la fecha actual en formato iso 
    def retrieve(self, request, pk=None):
    	# Definimos la instancia
        obj = FechaHora()	
        # Almacenamos el valor de fecha actual en formato iso
        obj.hora_actual=datetime.datetime.now().isoformat()
        # Serializamos la instancia para su transporte
        serializer = FechaHoraSerializer(obj)
        # Retornamos la informacion
        return Response(serializer.data)