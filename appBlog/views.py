from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from appBlog.models import Blog, Categorias #importamos los modelos de la appBlog
# Create your views here.
from proyecto_rein.forms import FormRegistrarEntrada

def blog(request):
    
    blogs=Blog.objects.all()#importa todas las entradas de blog
    categoria=Categorias.objects.all()

    return render(request,"appBlog/blog.html",{
        'blogs':blogs,
        'categorias':categoria})

def registrarnuevaentrada(request):

    form_registrarnuevaentrada = FormRegistrarEntrada(request.POST or None)

    if request.method == 'POST' and form_registrarnuevaentrada.is_valid():

        tituloE=form_registrarnuevaentrada.cleaned_data.get('tituloEntrada')
        contenidoE=form_registrarnuevaentrada.cleaned_data.get('contenidoEntrada')
        # categoriaE=registrarnuevaentrada.cleaned_data.get('categoriasEntrada')
        imagenE=form_registrarnuevaentrada.cleaned_data.get('imagenDestacada')

        nuevo=Blog.objects.create(titulo=tituloE,descripcion=contenidoE,imagen='autismo.jpg')

        if nuevo:
            nuevo.save()
            messages.success(request,'Entrada creada con exito')
            return redirect('blog')
        else:
            print('error al guardar la informacion')

  



    return render(request,'appBlog/nuevaentrada.html',{

        'registrarnuevaentrada': form_registrarnuevaentrada

    })