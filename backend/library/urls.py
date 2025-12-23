from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
    path('lista_livros/', views.lista_livros, name='lista_livros'),
    path('editar_livro/<int:pk>', views.editar_livro, name='editar_livro'),
    path('deletar_livro/<int:pk>', views.deletar_livro, name='deletar_livro'),
]