from django.shortcuts import render, redirect
from .forms import ContactFormForm
from .models import ContactForm, Flan

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

def contacto(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            ContactForm(**form.cleaned_data).save()
            return redirect('exito')
    else:
        form = ContactFormForm()
    return render(request, 'contact.html', {
        'form': form
    })

def exito(request):
    return render(request, 'success.html', {})