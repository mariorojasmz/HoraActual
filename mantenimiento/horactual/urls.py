from django.conf.urls import * 
from horactual import views

urlpatterns = [  
	 #Recuperamos el valor hora actual con viewSet get : retrieve
	url(r'^',views.FechaHoraViewSet.as_view({'get': 'retrieve'})), 
]

 