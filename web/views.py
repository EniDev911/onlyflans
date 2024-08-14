from django.shortcuts import render
from .models import Flan

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {
        'flanes_publicos': flanes_publicos
    })

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {
        'flanes_privados': flanes_privados
    })
