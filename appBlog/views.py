from django.shortcuts import render
from appBlog.models import Blog, Categorias #importamos los modelos de la appBlog
# Create your views here.

def blog(request):
    
    blogs=Blog.objects.all()#importa todas las entradas de blog
    categoria=Categorias.objects.all()

    return render(request,"appBlog/blog.html",{
        'blogs':blogs,
        'categorias':categoria})

def nuevaentrada(request):
    return render(request,'appBlog/nuevaentrada.html',{

    })