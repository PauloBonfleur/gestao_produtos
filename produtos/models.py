from django.db import models
import datetime
# Create your models here.


class Produto(models.Model):
    Produto = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30)
    Número_de_série = models.IntegerField()
    Quantidade = models.IntegerField()
    Preço = models.DecimalField(max_digits=7, decimal_places=2)
    Descrição = models.TextField()
    Foto = models.ImageField(upload_to='produto_fotos', null=True, blank=True)
    Data = models.DateField(default=datetime.datetime.now)

    def __str__(self):
        return self.Produto

