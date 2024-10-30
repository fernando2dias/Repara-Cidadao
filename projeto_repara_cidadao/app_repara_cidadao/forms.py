from django import forms
from .models import Reparo

class ReparoModelForm(forms.ModelForm):

    class Meta:
        model = Reparo
        fields = ['reparo', 'rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'referencia', 'imagem']