from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ContactFormForm
from .models import ContactForm, Flan

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {
        'flanes_publicos': flanes_publicos
    })

def acerca(request):
    return render(request, 'about.html', {})

@login_required
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

def detalle(request, id):
    flan = get_object_or_404(Flan, id=id)
    return render(request, 'detail.html', {'flan': flan})