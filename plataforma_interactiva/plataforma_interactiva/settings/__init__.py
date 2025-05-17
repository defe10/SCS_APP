import os

# Lee la variable de entorno DJANGO_ENV
settings_env = os.environ.get("DJANGO_ENV")

# Según su valor, importa los ajustes correspondientes
if settings_env == "production":
    from .settings_prod import *
else:
    from .settings_local import *
