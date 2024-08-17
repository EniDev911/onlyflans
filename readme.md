# ONLYFLANS - HITO II

## REQUERIMIENTO 1

Crear modelo Flan, generar y aplicar sus migraciones y agregar el modelo al panel de administración. Agrega al menos 8 elementos de Flan.

```py
# web/models.py
from django.db import models
import uuid # UUID aleatorio al crear instancia

class Flan(models.Model):
flan_uuid = models.UUIDField(default=uuid.uuid4)
name = models.CharField(max_length=50, null=False)
description = models.TextField()
image_url = models.URLField()
slug = models.SlugField(max_length=50, unique=True, blank=True)
is_private = models.BooleanField()
```

Registramos el modelo en el panel administrativo.

```py
# web/admin.py
from django.contrib import admin
from .models import Flan # Importamos el modelo Flan.

admin.site.register(Flan)
```

## REQUERIMIENTO 2

Mostrar tus flanes recién creados al público. Agrégale el resultado de todos los Flanes existentes en tu sitio web como contexto a tu vista de la ruta “indice” e imprime los resultados a través de la plantilla index.html por medio de componentes cards de bootstrap, utilizando un ciclo for de las plantillas de django para mostrar cada uno de los Flan anteriormente creados.
En la página “indice” se mostrarán solo los Flan cuyo atributo is_private es False.
En la página “welcome”, se mostrarán solo los Flan cuyo atributo is_private es True.

Enviamos el contexto al template para accederlo. Obtenemos todos los objetos (registros) desde la bd sqlite.

```py
web/views.py
from django.shortcuts import render
from .models import Flan

def indice(request):
flans = Flan.objects.all()
return render(request, 'index.html', {
'flans': flans
})
```

```html
<!-- web/templates/includes/card.html -->
<div class="card shadow-sm mb-3 border">
  <img src="{{ img }}" alt="{{ name }}" class="card-img-top" />
  <div class="card-body">
    <h5 class="card-title">{{ name }}</h5>
    <p class="card-text">{{ desc }}</p>
  </div>
</div>
```

Utilizamos el fragmento del componente card de bootstrap y le pasamos los parámetros con with

```html
<!-- web/templates/pages/index.html -->
{% extends "base.html" %} {% block content %}

<h2>Índice</h2>
<div class="container my-4">
  <div class="row">
    {% for flan in flans %}
    <div class="col-12 col-md-6 col-lg-3">
      {% include "card.html" with name=flan.name image=flan.image_url
      desc=flan.description %}
    </div>
    {% endfor %}
  </div>
</div>
{% endblock %}
```

- Enviamos al contexto sólo aquellos flanes que su atributo is_private sea False.
- Enviamos al contexto sólo aquellos flanes que su atributo is_private sea True.

```py
# web/views.py
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
```

Recorremos los flanes públicos en el template index.html:

```html
<!-- web/templates/pages/index.html -->
{% for flan in flanes_publicos %}

<div class="col-12 col-md-6 col-lg-3">
  {% include "card.html" with name=flan.name image=flan.image_url
  desc=flan.description %}
</div>
{% endfor %}
```

Recorremos los flanes privados en el template welcome.html:

```html
<!-- web/templates/pages/welcome.html -->
{% for flan in flanes_privados %}
<div class="col-12 col-md-6 col-lg-3">
  {% include "card.html" with name=flan.name image=flan.image_url
  desc=flan.description %}
</div>
{% endfor %}
```

## REQUERIMIENTO 3

Crear el modelo ContactForm, generar y aplicar sus migraciones y agregar el modelo al panel de administración de Django.

Construir un formulario personalizado utilizando la clase Form y que contenga los atributos necesarios para recibir los datos.
En la vista contacto, debemos realizar las validaciones correspondientes y crear un nuevo objeto del modelo ContactForm basado en el formulario.

| Atributo       | Tipo              | Anotaciones     |
| :------------- | :---------------- | :-------------- | --------------------------------------- |
| ````           | contact_form_uuid | UUIDField       | default = uuid.uuidd4, editable = False |
| customer_email | EmailField        |                 |
| customer_name  | CharField         | max_length = 64 |
| message        | TextField         |                 |

Definición del modelo ContacForm, según el requerimiento:

```py
# web/models.py
class ContactForm(models.Model):
  contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
  customer_email = models.EmailField()
  customer_name = models.CharField(max_length=64)
  message = models.TextField()
```

Registramos el modelo en el panel administrativo:

```py
# web/admin.py
from django.contrib import admin
from .models import Flan, ContactForm

admin.site.register(Flan)
admin.site.register(ContactForm)
```

Definimos un formulario personalizado, utilizando la clase Form:

```py
# web/forms.py
from django import forms

class ContactFormForm(forms.Form):
  customer_email = forms.EmailField(label="Correo")
  customer_name = forms.CharField(max_length=64, label="Nombre")
  message = forms.CharField(label="Mensaje")
```

Importamos el formulario, y lo pasamos al contexto del template:

```py
# web/views.py
from django.shortcuts import render, redirect
from .forms import ContactFormForm
from .models import ContactForm, Flan

def contacto(request):
  if request.method == "POST":
    form = ContactFormForm(request.POST)
    if form.is_valid(): # Procesamos los datos y creamos un nuevo objeto en la bd
      ContactForm(**form.cleaned_data).save()
      return redirect('exito') # 👈 Pronto configuraremos esta página
  else:
    form = ContactFormForm()
    return render(request, 'contact.html', {
      'form': form
    })
```

```html
<!-- web/templates/pages/contact.html -->
{% extends 'base.html' %} {% block content %}

<form method="post">
  {% csrf_token %} {{ form.as_p }}
  <button type="submit">Enviar</button>
</form>
{% endblock %}
```

Agregamos la url a la barra de navegación:

```html
templates/includes/navbar.html

<nav class="navbar navbar-expand-lg bg-body">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-target="#navbar" data-bs-toggle="collapse">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbar">
      <div class="navbar-nav me-auto mb-2 mb-lg-0">
        <a class="nav-link" aria-current="page" href="{% url "indice" %}">Índice</a>
        <a class="nav-link" href="{% url "acerca" %}">Acerca</a>
        <a class="nav-link" href="{% url "bienvenido" %}">Bienvenido</a>
        <a class="nav-link" href="{% url "contacto" %}">Contacto</a>
      </div>
    </div>
  </div>
</nav>
```

Finalmente, configuramos la URL en urls.py para que la vista sea accesible:

```py
onlyflans/urls.py
from django.contrib import admin
from django.urls import path
from web.views import indice, acerca, bienvenido, contacto

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', indice, name='indice'),
  path('acerca', acerca, name='acerca'),
  path('bienvenido', bienvenido, name='bienvenido'),
  path('contacto', contacto, name='contacto'),
]
```

Definimos una vista para renderizar una plantilla de exito:

```py
# web/views.py
def exito(request):
  return render(request, 'success.html', {})

```

Configuramos otra URL en urls.py para que la vista sea accesible:

```py
onlyflans/urls.py
from web.views import ..., exito

urlpatterns = [
...
path('exito', exito, name='exito'),
]
```

Añadimos contenido a la plantilla:

```html
<!-- web/templates/pages/success.html -->
{% extends "base.html" %} {% block content %}

<div class="my-5 text-center fs-3">
  Gracias por contactarte con OnlyFlans<br />
  te responderemos en breve<br />
  <a href="{% url 'indice' %}" class="btn btn-primary">Volver a inicio</a>
</div>
{% endblock %}
```
