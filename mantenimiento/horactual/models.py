from __future__ import unicode_literals 
from django.db import models 

  # Mario Rojas: Clase FechaHora contiene un solo campo donde se almacena la fecha actual del servidor.
class FechaHora(models.Model):
 
	hora_actual=''
