from django.db import models
from django.contrib.auth.models import User

class Receita(models.Model):
    CATEGORIAS = [
        ('DOCES', 'Doces'),
        ('SALGADOS', 'Salgados'),
        ('MASSAS', 'Massas'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.PositiveIntegerField(help_text="Em minutos")
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=8, choices=CATEGORIAS)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)

    def __str__(self):
        return self.titulo