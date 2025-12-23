from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CadastroForm, LoginForm
from django.contrib.auth import login


def cadastro_usuario(request):
    """
    View responsável apenas por:
        - Orquestrar requisição e resposta
        - Delegar validações ao formulário
        - Persistir o usuário quando válido
    """

    form = CadastroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        return redirect('login')
    
    return render(request, 'cadastro.html', {'form': form})


def login_usuario(request):
    """
    View responsável apenas por autenticar e iniciar a sessão.
    """

    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        login(request, form.user)
        return redirect('library:cadastro_livro')
    
    return render(request, 'login.html', {'form': form})
