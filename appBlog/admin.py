from django.contrib import admin
from .models import Blog, Categorias #importamos el modelo de la appBlog
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
     readonly_fields=('created','updated')


class blogAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Blog, blogAdmin)
admin.site.register(Categorias,CategoriaAdmin)

