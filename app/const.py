# Importamos libreria para leer el sistema operativo
import os

# Obtenemos las variables de entorno
CONN_STRING = os.getenv(
  "DATABASE_URL"
)  # Obtenemos la cadena de conexión a la base de datos desde las variables de entorno
