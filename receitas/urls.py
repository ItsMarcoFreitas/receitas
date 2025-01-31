from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_receitas, name='lista_receitas'),
    path('receita/<int:receita_id>/', views.detalhe_receita, name='detalhe_receita'),
]