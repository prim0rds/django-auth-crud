# Sistema de Gerenciamento de Biblioteca

Projeto desenvolvido em Django para cadastro, edição e organização de livros, com sistema de autenticação completo e interface moderna em tema dark.

## Funcionalidades

- Cadastro e login de usuários
- Logout seguro
- Cadastro, edição e exclusão de livros
- Interface moderna com tema dark
- Layout responsivo
- Proteção CSRF
- Validações no backend com Django Forms

## Tecnologias

- Python 3.12
- Django 5
- HTML5 + CSS3
- SQLite (padrão)

## Instalação

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse: http://127.0.0.1:8000

## Estrutura

```
accounts/        # autenticação
library/         # gerenciamento de livros
templates/       # templates HTML
static/css/      # estilos por página
```

## Autor

Felipe Silva

Projeto educacional para estudo de Django e desenvolvimento web.
