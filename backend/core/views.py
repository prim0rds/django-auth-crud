from django.shortcuts import render

def home(request):
    """
    Página incial do site.
    Responsável apenas pela apresentação e navegação.
    """

    return render(request, 'home.html')
