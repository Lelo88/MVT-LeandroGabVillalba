from django.urls import path
from Familia.views import agrega_familiar, muestra_familia, inicio


urlpatterns = [
    path('agrega-familiar/<nombre>/<apellido>/<fecha_nac>',agrega_familiar,name='Agregado'),
    path('inicio/', inicio, name='Inicio'),
    path('listado-familiar/',muestra_familia, name='Listado2')
]
