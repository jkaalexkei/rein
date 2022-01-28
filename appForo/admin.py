from django.contrib import admin
from . models import Categoria_foro,Foro
# Register your models here.

class CategoriaForoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ForoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Categoria_foro,CategoriaForoAdmin)
admin.site.register(Foro,ForoAdmin)


