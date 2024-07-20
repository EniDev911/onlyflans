# ONLFLANS - HITO I

## REQUERIMIENTO 1

Crea un entorno virtual llamado onlyflans y una vez activado, comprueba la versión de python usada.

Aquí creamos el entorno virtual y lo activamos en un solo paso con [Pipenv](https://pipenv-es.readthedocs.io/es/latest/):

```bash
pipenv shell
```

Aquí revisamos la versión de Python que tenemos:

```bash
python --version # Windows
python3 --version # Unix
```

## REQUERIMIENTO 2

Instalar Django 3.2.4 dentro del entorno virtual onlyflans, una vez instalado verifica que haya sido instalado exitosamente con el comando pip freeze.

Aquí instalamos django 3.2.4:

```bash
pipenv install django==3.2.4
```

Verificamos la instalación:

```bash
pip freeze
```

## REQUERIMIENTO 3

Usando django-admin genera un proyecto llamado onlyflans, una vez creado ingresa a la carpeta del proyecto generado, aplica las migraciones y ejecuta el servidor utilizando los comandos correspondientes del archivo manage.py y accede a la url disponible para tu proyecto. Una vez puedas acceder a la web desde el navegador, realiza una captura.

Aplicamos las migraciones:

```bash
python manage.py migrate
```

Corremos el servidor:

```bash
python manage.py runserver
```

[Presentación](https://docs.google.com/presentation/d/e/2PACX-1vSNxHthQzr0wh5ingHrEwuZZndhA92bHL4M533VBiJS4hD6MUIZOfBdAwKZ0ckLvkHce-8j12ViMe5I/embed?start=false&loop=false&delayms=3000&slide=id.g2eb77851c08_0_0)
