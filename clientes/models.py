from django.db import models

# Create your models here.

class Cliente(models.Model):
    idcliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=15)
    data_de_nascimento = models.DateField()
    endereço = models.CharField(max_length=200)

    def __str__(self):
        return self.nome