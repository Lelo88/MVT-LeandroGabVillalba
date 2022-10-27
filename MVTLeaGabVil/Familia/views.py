from datetime import datetime
from django.shortcuts import render, redirect
from .models import Familiar
from django.http import HttpResponse
from django.template import loader
from .forms import Familiares
# Create your views here.

def agrega_familiar(request, nombre, apellido, fecha_nac):
    
    familiar = Familiar(nombre=nombre, apellido=apellido)    
    
    dia_nac = datetime.strptime(fecha_nac, '%Y-%m-%d').date()
    
    familiar.fecha_nac = dia_nac
    
    familiar.save()

    plantilla=loader.get_template('agrega_familiar.html')    
    documento=plantilla.render({"name": familiar.nombre, "surname": familiar.apellido, "birth_date": familiar.fecha_nac} )
    
    return HttpResponse(documento)

def muestra_familia(request):

    familia = Familiar.objects.all()

    return render(request, 'listado_familiar.html',{"lista_familia": familia})

def inicio(request):
    
    return render(request,'inicio.html')

def familiares(request):
    if request.method == 'POST':
        familia=Familiares(request.POST)
        
        if familia.is_valid():
            informacion = familia.cleaned_data
            familiar = Familiar(nombre=informacion['nombre'], apellido=informacion['apellido'], fecha_nac = informacion['fechanac'])
            familiar.save()
            
            return redirect('Listado2')
            #return render(request, 'inicio.html')
    else:
        familia = Familiares()
        
    return render(request, 'formularioFamilia.html', {'familiar': familia})
        