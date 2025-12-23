from django import forms
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'descricao', 'publicado_em']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título do livro'
            }),

            'autor': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Autor'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição'
            }),

            'publicado_em': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }