# ONLYFLANS - HITO II

## REQUERIMIENTO 1

Inicia una app de Django llamada web dentro del proyecto onlyflans y agrégala a la lista de aplicaciones instaladas, dentro de ella crea una carpeta templates que contenga un archivo llamado index.html que contenga la estrcutura `<html>`, `<header>` y `<body>`. Dentro del `<body>` escribe el texto “índice”. Crea 2 copias del archivo index.html, llamadas about.html y welcome.html y reemplace el texto de sus estructuras `<body>` por “acerca” y “bienvenido cliente” respectivamente.

Aquí se crea la nueva app📦:

```bash
python manage.py startapp web
```

Aquí se registra la app en el proyecto:

```py
# onlyflans/settings.py
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web'
]
```

Creamos las plantillas:

```bash
mkdir -p web/templates
touch web/templates/index.html
touch web/templates/about.html
touch web/templates/welcome.html
```

Nos quedaría la estructura de la siguiente forma en el explorador:

```bash
📂web
 └── 📂templates
      ├── 📄about.html
      ├── 📄index.html
      └── 📄welcome.html
```


Escribimos contenido en la plantillas:

```html
<!-- templates/index.html -->
<html>
<body>
<header><header>
  Índice
</body>
</html>

<!-- templates/about.html -->
<html>
<body>
<header><header>
  Acerca
</body>
</html>

<!-- templates/Welcome.html -->
<html>
<body>
<header><header>
  Bienvenido cliente
</body>
</html>
```

## REQUERIMIENTO 2

Habilitar las 3 urls distintas con una plantilla básica que muestre solo texto, esto implica:

- Mostrar el texto “índice” en la ruta /
- Mostrar el texto “acerca” en la ruta /acerca
- Mostrar el texto “bienvenido cliente” en la ruta /bienvenido

Una vez realizado, ejecuta el sitio web con `python manage.py runserver`. 

```py
# web/views.py
from django.shortcuts import render

def indice(request):
    return render(request, 'index.html', {})

def acerca(request):
    return render(request, 'about.html', {})

def bienvenido(request):
    return render(request, 'welcome.html', {})
```
```py
# onlyflans/urls.py
from django.contrib import admin
from django.urls import path
from web.views import indice, acerca, bienvenido

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indice, name='indice'),
    path('acerca', acerca, name='acerca'),
    path('bienvenido', bienvenido, name='bienvenido'),
]
```

## REQUERIMIENTO 3

Crear una plantilla base llamada base.html que contenga los elementos comunes a todas las rutas necesarias para el sitio web, esto puede ser como en el caso anterior, simplemente un texto que identifique cada elemento, por ejemplo:

- Mostrar el texto “índice” en el lugar donde iría el header
- Mostrar el texto “navbar” en el lugar donde iría la barra de navegación
- Mostrar el texto “footer” en el lugar donde iría el footer

Debes valerte de estructura como `<div>` para separar los distintos elementos y agregar un color de fondo para guiar mejor la estructura general. 


```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
    <title>
     {% block title %}OnlyFlans{% endblock %}
    </title>
  </head>
  <body>
    <div style="background: red">header</div>
    <div style="background: yellow">navbar</div>
    <div>contenido</div>
    <div style="background: green">footer</div>
  </body>
</html>

<!-- templates/index.html -->
{% extends "base.html" %}
{% block title %}Índice{% endblock %}

<!-- templates/about.html -->
{% extends "base.html" %}
{% block title %}Acerca{% endblock %}

<!-- templates/welcome.html -->
{% extends "base.html" %}
{% block title %}
Bienvenido
{% endblock %}
```

Visitamos las siguientes url:

- 127.0.0.1:8000
- 127.0.0.1:8000/bienvenido
- 127.0.0.1:8000/acerca

## REQUERIMIENTO 4

Crear las vistas y plantillas personalizadas, añadiendo componentes de bootstrap que permitan crear un sitio más “atractivo” en cuanto al contenido, acercándose a lo requerido, para esto debemos realizar lo siguiente:

“Instalar” bootstrap a través de la plantilla inicial de bootstrap en la plantilla base, complementando su estructura <body> con lo que ya existe en el archivo. Luego cambiamos el contenido de la estructura <title> por “Bienvenido a onlyflans”.
Utilizar ya sea el sistema de grilla o la clase container al contenido de la web en el archivo base.html.


```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}Bienvenido a OnlyFlans{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="sty…"/>
  </head>
  <body>
    <div style="background: red">header</div>
    <div style="background: yellow">navbar</div>
    <div>contenido</div>
    <div style="background: green">footer</div>
    <script src="//cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js></script>
  </body>
</html>
```

Para una mejor organización, incluiremos, los siguientes directorios en la lista para que estén disponible en el sistema de plantilla.

```py
# onlyflans/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'web/templates/includes/'),
                 os.path.join(BASE_DIR, 'web/templates/pages/')
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
               …
            ],
        },
    },
]
```

```html
<!-- web/templates/includes/navbar.html -->
<nav class="navbar navbar-expand-lg bg-body">
  <div class="container-fluid">
    <button class="navbar-toggler" 
      type="button" data-bs-target="#navbar"
      data-bs-toggle="collapse" aria-controls="navbar" aria-exp=…>
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbar">
      <div class="navbar-nav me-auto mb-2 mb-lg-0">
        <a class="nav-link" aria-current="page" href="{% url 'indice' %}">Índice</a>
        <a class="nav-link" href="{% url 'acerca' %}">Acerca</a>
        <a class="nav-link" href="{% url 'bienvenido' %}">Bienvenido</a>
      </div>
    </div>
  </div>
</nav>

<!-- web/templates/base.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
   ...
  </head>
  <body>
   ...
   {% include "navbar.html" %}
  </body>
</html>
```
