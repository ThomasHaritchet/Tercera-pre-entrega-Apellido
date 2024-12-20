# Proyecto Django - Tercera Pre-entrega

Este es un proyecto web realizado con **Django**, utilizando el patrón **MVT**. El proyecto incluye modelos de base de datos, formularios para insertar y buscar datos, y herencia de plantillas HTML.


Funcionalidades
Insertar datos: Utiliza los formularios para insertar información en la base de datos.
Buscar datos: Puedes buscar los datos guardados.
Herencia de plantillas: El proyecto usa herencia de plantillas HTML.


   ```bash
   git clone https://github.com/ThomasHaritchet/Tercera-pre-entrega-Apellido.git
Instalar dependencias:

Navega a la carpeta del proyecto y crea un entorno virtual:

bash
Copiar código
cd Tercera-pre-entrega-Apellido
python -m venv env
source env/bin/activate  
pip install django
Ejecutar migraciones:

bash
Copiar código
python manage.py migrate
Iniciar el servidor:

bash
Copiar código
python manage.py runserver
Accede al proyecto en: http://127.0.0.1:8000/

Estructura del proyecto

Tercera-pre-entrega-Apellido/
│
├── myapp/                 # Carpeta con la aplicación principal
│   ├── migrations/        # Migraciones de la base de datos
│   ├── models.py          # Los modelos de la base de datos
│   ├── views.py           # Las vistas
│   ├── templates/         # Plantillas HTML
│   └── forms.py           # Formularios
│
├── myproject/             # Configuración de Django
│   ├── settings.py        # Configuraciones generales
│   └── urls.py            # Rutas del proyecto
│
└── manage.py              # Archivo principal para ejecutar el proyecto


