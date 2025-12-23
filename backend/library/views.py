from django.shortcuts import render, redirect
from .forms import LivroForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='accounts:login')
def cadastro_livro(request):
    """
    View para cadastrar um livro.
    Apenas usuários logados podem acessar.
    """
    form = LivroForm(request.POST or None)
  
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Livro cadastrado com sucesso!')
        return redirect('library:cadastro_livro')
    
    return render(request, 'cadastro_livro.html', {'form': form})