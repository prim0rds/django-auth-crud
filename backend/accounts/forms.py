from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CadastroForm(forms.Form):
    """
    Formulário responsável por:
        - Capturar os dados
        - Validar regras de negócio
        - Garantir integridade
    
    A view deve permanecer enxuta, delegando
    toda a lógica de validação para este formulário.
    """

    username = forms.CharField(
        label='Usuário',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu usuário'
        })
    )

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail'
        })
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )

    password_confirm = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(attrs={
            'class': 'forms-control',
            'placeholder': 'Confirme sua senha'
        })
    )


    def clean_username(self):
        """
        Garante unicidade do nome de usuário.
        """
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise ValidationError('Usuário já cadastrado.')
        
        return username
    

    def clean_email(self):
        """
        Garante que o e-mail não esteja associado
        a outro usuário no sistema.
        """
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise ValidationError('E-mail já cadastrado')
        
        return email


    def clean(self):
        """
        Validação cruzada entre os campos de senha.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'As senhas não coincidem.')