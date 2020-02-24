from warnings import onceregistry

from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255 , blank = True)
    descricao = models.TextField()
    categoria  = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True,upload_to='fotos/%Y/%M/%D')
    def __str__(self):
        return self.nome
