from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('cadastro_livro/', views.cadastro_livro, name='cadastro_livro'),
]