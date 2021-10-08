from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   ...


class Lista(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField('Novo', max_length=250)
    feito = models.BooleanField(default=False)
    data = models.DateField("Data:")
    hora = models.TimeField("Hora")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_modificacao =models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Usuário {self.usuario} - Lista {self.item}'

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
