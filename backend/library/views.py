from django.shortcuts import render, redirect, get_object_or_404
from .forms import LivroForm
from .models import Livro
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='accounts:login')
def cadastro_livro(request):
    form = LivroForm(request.POST or None)
  
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Livro cadastrado com sucesso!')
        return redirect('library:cadastro_livro')
    
    return render(request, 'cadastro_livro.html', {'form': form})

@login_required(login_url='accounts:login')
def lista_livros(request):
    livros = Livro.objects.all().order_by('-criado_em')
    return render(request, 'lista_livros.html', {'livros': livros})


@login_required(login_url='accounts:login')
def editar_livro(request, pk):
    if request.method == 'POST':
        livro = get_object_or_404(Livro, pk=pk)
        livro.titulo = request.POST.get('titulo', livro.titulo)
        livro.autor = request.POST.get('autor', livro.autor)
        livro.descricao = request.POST.get('descricao', livro.descricao)
        publicado_em = request.POST.get('publicado_em')
        if publicado_em:
            livro.publicado_em = publicado_em
        livro.save()
    
    return redirect('library:lista_livros')


@login_required(login_url='accounts:login')
def deletar_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    livro.delete()
    return redirect('library:lista_livros')
    