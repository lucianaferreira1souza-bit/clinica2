from django.db import models

# Create your models here.

class Medico(models.Model):
    idmedico = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.nome