# PLATAFORMA INTERACTIVA 
Desarrollado por: Federico Casoni


La Plataforma Interactiva es una herramienta digital diseñada para enriquecer la experiencia de los asistentes al festival cinematográfico **29º Semana de Cine en Salta.**
A través de un sitio web accesible desde dispositivos móviles,los usuarios pueden participar en actividades interactivas como trivias, votaciones y encuestas, fomentando su involucramiento y proporcionando datos valiosos 
para los organizadores del evento. Además podrán acceder a la programción del festival.
Se accede a la plataforma escaneando un código QR, lo que garantiza una experiencia rápida y sencilla.


# FUNCIONALIDADES:

1. Trivias:
   - Preguntas sobre el cine salteño.
   - Muestra una pregunta a la vez con imagen de la película que hacer referencia la pregunta
   - Los usuarios reciben retroalimentación inmediata y pueden jugar varias trivias.
   - Puntaje con resumen final

2. Voto del Público:
   - Los usuarios pueden calificar las películas salteñas del festival: no me gustó, me gustó poco, me gustó, me gustó mucho.
   - Las respuestas se almacenan para su posterior análisis.

3. Encuestas:
   - Es igual a voto del público pero con las secciones del festival y otros aspectos.

4. Programación:
   - Consiste a un acceso directo a la sección de programación de la web oficial del festival
   

# TECNOLOGÍA
  - Django 5.1
  - Bootstrap 5
  - HTML + CSS personalizado
  - SQLite (por ahora)


# LOGIN
  - Requiere email, nombre de usuario y contraseña, para que no voten más de una vez.


# PARA QUE FUNCIONE:
  - git clone https://github.com/tuusuario/scs_app.git
  - cd scs_app
  - python -m venv env
  - source env/bin/activate 
  - pip install -r requirements.txt 
  - python manage.py migrate
  - python manage.py createsuperuser
  - python manage.py runserver

# CAPTURAS

![Captura de pantalla 2025-04-18 a la(s) 4 28 36 p  m](https://github.com/user-attachments/assets/94072342-d03d-4362-ace8-7b6907d540f8)
![Captura de pantalla 2025-04-18 a la(s) 4 26 21 p  m](https://github.com/user-attachments/assets/7bea196a-8ea9-4000-bc22-4a7f49ca998c)
![Captura de pantalla 2025-04-18 a la(s) 4 26 36 p  m](https://github.com/user-attachments/assets/28512f9b-dbcf-4933-82a6-288f2f929dc0)
![Captura de pantalla 2025-04-18 a la(s) 4 26 54 p  m](https://github.com/user-attachments/assets/d394798e-04f3-4797-ab05-88c6082cd172)
![Captura de pantalla 2025-04-18 a la(s) 4 27 14 p  m](https://github.com/user-attachments/assets/b0a5eccf-6e37-46e7-8fea-a5a6cffd904c)
![Captura de pantalla 2025-04-18 a la(s) 8 58 19 p  m](https://github.com/user-attachments/assets/ee0bd93c-8608-4888-a0d6-a7ff9d5b0e9f)
