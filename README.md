# PLATAFORMA INTERACTIVA 
Desarrollado por: Federico Casoni


La Plataforma Interactiva es una herramienta digital diseñada para enriquecer la experiencia de los asistentes al festival cinematográfico **29º Semana de Cine en Salta**
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

![Captura de pantalla 2025-04-17 a la(s) 6 15 04 p  m](https://github.com/user-attachments/assets/17956891-2cba-4912-a667-6501c642ff36)
![Captura de pantalla 2025-04-17 a la(s) 6 15 17 p  m](https://github.com/user-attachments/assets/ae1dd43a-43ed-4711-85af-b1e616bad0d1)
![Captura de pantalla 2025-04-17 a la(s) 6 15 46 p  m](https://github.com/user-attachments/assets/7fe2f85e-29fa-4091-b4b9-b53c39715da5)
![Captura de pantalla 2025-04-17 a la(s) 6 16 05 p  m](https://github.com/user-attachments/assets/d9170a9b-b94c-494a-9c52-026fb2409167)
