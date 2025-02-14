from django.shortcuts import render, get_object_or_404
from .models import Receita

def lista_receitas(request):
    receitas = Receita.objects.all().order_by('-data_publicacao')
    return render(request, 'home.html', {'receitas': receitas})

def detalhe_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'receita_detalhe.html', {'receita': receita})