from django.forms import ModelForm
from .models import Produto


class Produtoform(ModelForm):
    class Meta:
        model = Produto
        fields = ['Produto', 'Categoria', 'Número_de_série', 'Quantidade', 'Preço', 'Descrição', 'Foto', 'Data']
