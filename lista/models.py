from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import send_email
from django.dispatch import receiver
from core import settings
from django.db.models.signals import post_save

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

@receiver(post_save, sender=User)
def novo_usuario(sender, instance, created, **kwargs):
    if created:
        msg = 'Um novo Usuário foi cadastrado! Verifique no admin do sistema'
        send_email('Novo usuário Cadastrado',msg )


post_save.connect(novo_usuario, sender=settings.AUTH_USER_MODEL)
