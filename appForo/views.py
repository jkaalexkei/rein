from django.shortcuts import render
from appForo.models import Foro,Categoria_foro

# Create your views here.

def foro(request):

    foropublicacion=Foro.objects.all()
    categoriaforo=Categoria_foro.objects.get(id='1')
    entradaforo = Foro.objects.filter(categoriasforo=categoriaforo)
    


    return render(request,"appForo/foro.html",{'foro':foropublicacion,'categoria':entradaforo})