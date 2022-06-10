from django.db import models

# Create your models here.

class Cadastro(models.Model):
    cep=models.CharField(max_length=9)
    endereco=models.TextField()
    numero=models.IntegerField()
    complemento=models.CharField(max_length=40)
    bairro=models.CharField(max_length=40)
    cidade=models.CharField(max_length=40)
    uf=models.CharField(max_length=2)
    descricao=models.TextField()
