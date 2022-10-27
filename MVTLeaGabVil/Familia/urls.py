from django.urls import path
from Familia.views import agrega_familiar, muestra_familia, inicio, familiares


urlpatterns = [
    path('agrega-familiar/<nombre>/<apellido>/<fecha_nac>',agrega_familiar,name='Agregado'),
    path('', inicio, name='Inicio'),
    path('listado-familiar/',muestra_familia, name='Listado2'),
    path('formulario-familia/',familiares, name='Familiares')
]
