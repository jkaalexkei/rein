from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# from appBlog.models import Blog #importamos los modelos de la appBlog
# Create your views here.

def home(request):

    return render(request,"appRein/home.html")

# def blog(request):

#     blogs=Blog.objects.all()#importa todas las entradas de blog

#     return render(request,"appRein/blog.html",{'blogs':blogs})


# def foro(request):
#      return render(request,"appRein/foro.html")

def calendario(request):
     return render(request,"appRein/calendario.html")

def iniciarsesion(request):

     # if request.method=='POST':
     #      messages.success(request,f"{username} Te has logueado correctamente")

     if request.method == 'POST':
          usuario = request.POST.get('username')
          clave = request.POST.get('password')

          user = authenticate(username=usuario,password=clave)

          if user:
               login(request,user)
               nombreusuario=User.objects.all()

               for usr in nombreusuario:
                    if usr.username == usuario:
                         messages.success(request,'Hola {}'.format(usr.first_name))
                         return redirect ('home')
                         
                    
               
          else:
               messages.error(request,'Usuario o Clave Inválida')
               print('usuario no autenticado')
          
     

     return render(request,"appRein/login.html")

def cerrarsesion(request):

     logout(request)
     messages.success(request,'Sesión Finalizada con exito')
     print('sesion cerrada')
     return redirect('home')
