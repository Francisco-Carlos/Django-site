from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Livros(models.Model):
    Titulo =models.CharField(max_length=100)
    Categoria = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='capas')
    Resumo = models.TextField()
    Valor = models.IntegerField()
    active = models.BooleanField(default=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta():
        db_table = 'Titulo'

    def __str__(self):
        return self.Titulo

