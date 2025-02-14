from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data_publicacao', 'autor')
    search_fields = ('titulo', 'descricao')
    list_filter = ('categoria', 'data_publicacao')