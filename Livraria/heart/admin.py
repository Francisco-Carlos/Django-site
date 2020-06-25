from django.contrib import admin
from .models import Livros
# Register your models here.

class LivroAdm(admin.ModelAdmin):
    list_display = ('id','Titulo','Categoria')

admin.site.register(Livros,LivroAdm)