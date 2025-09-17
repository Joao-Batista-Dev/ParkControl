from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(
        User, # usando o user do django
        on_delete=models.PROTECT, # protecao de caso for deleta usuario do django - ele avisar - gerar consistencia de dados
        blank=True, # black e null = True - para campo que não são obrigatorio
        null=True, 
        related_name='customers', # definir o relacionamento inverso 
        verbose_name='Cliente', # nome da classe do admin em portugues
    )
    name = models.CharField(
        max_length=150, 
        verbose_name='Nome',
    )
    cpf = models.CharField(
        max_length=15,
        null=True, 
        blank=True, 
        verbose_name='CPF',
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name='Telefone',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name='Criando em',
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name='Atualizado em',
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        
    def __str__(self):
        return self.name




