 
from django.conf.urls import *
from django.contrib import admin

urlpatterns = [
    # Mario Rojas: La ruta de la aplicacion horactual esta por defecto, http://127.0.0.1:8000/ 
	url(r'^', include('horactual.urls')), 
    # Mario Rojas: esta habilitado el portal de administracion
    url(r'^mantenimiento/admin/', admin.site.urls),
    # Mario Rojas: se incluye las rutas urls de la aplicacion
    url(r'^mantenimiento/horactual/', include('horactual.urls')),
]
