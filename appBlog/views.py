from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from appBlog.models import Blog, Categorias #importamos los modelos de la appBlog
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
# from django.http import HttpResponseRedirect
# Create your views here.
# from proyecto_rein.forms import Inputimagen

def blog(request):
    
    blogs=Blog.objects.all()#importa todas las entradas de blog
    categoria=Categorias.objects.all()

    return render(request,"appBlog/blog.html",{
         'blogs':blogs,
         'categorias':categoria
    })
    
       

def registrarnuevaentrada(request):

     if request.method == 'POST':
          tituloe = request.POST['tituloe']
          contenidoe = request.POST['contenidoe']
          categoriae = request.POST['categoriae']
          imagene = request.FILES['imagene']

          cat = Categorias.objects.create(nombre=categoriae)

          documento = Blog.objects.create(titulo=tituloe,descripcion=contenidoe,imagen=imagene,categoria=cat)
          documento.save()
          if documento:
               messages.success(request,'Información Guardada')
               return redirect('blog')
          

     return render(request,'appBlog/nuevaentrada.html',{})    
   
#    if request.method == 'POST':
#           usuario = request.POST.get('username')
#           clave = request.POST.get('password')

#           user = authenticate(username=usuario,password=clave)

#           if user:
#                login(request,user)
#                nombreusuario=User.objects.all()

#                for usr in nombreusuario:
#                     if usr.username == usuario:
#                         print(usr.first_name)
    
     
        
        #  'registrarnuevaentrada': form_registrarnuevaentrada

     

    # form_registrarnuevaentrada = FormRegistrarEntrada(request.POST or None)

    # if request.method == 'POST' and form_registrarnuevaentrada.is_valid():

    #     tituloE=form_registrarnuevaentrada.cleaned_data.get('tituloEntrada')
    #     contenidoE=form_registrarnuevaentrada.cleaned_data.get('contenidoEntrada')
    #     # categoriaE=registrarnuevaentrada.cleaned_data.get('categoriasEntrada')
    #    # imagenE=form_registrarnuevaentrada.get('imagenDestacada')

    #     nuevo=Blog.objects.create(titulo=tituloE,descripcion=contenidoE,imagen='autismo.jpg')

    #     if nuevo:
    #         nuevo.save()
    #         messages.success(request,'Entrada creada con exito')
    #         return redirect('blog')
    #     else:
    #         print('error al guardar la informacion')

  



    # return render(request,'appBlog/nuevaentrada.html',{

    #     'registrarnuevaentrada': form_registrarnuevaentrada

    # })