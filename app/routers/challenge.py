# Importamos la librería para conectarnos a Postgres
import psycopg
from fastapi import APIRouter

# Importamos la cadena de conexión desde las constantes
from app.const import CONN_STRING
from app.db.challenges_queries import (
  fetch_all_challenges,
  fetch_random_challenge,
  insert_challenge,
)

# Inicializamos el router de FastAPI para los retos
router = APIRouter(prefix="/challenge", tags=["challenge"])


# Definimos las rutas para manejar los retos
@router.get("/get_all_challenge")
async def get_challenge():
  # manejo de errores
  try:
    # abrimos una conexión a la db
    with psycopg.connect(CONN_STRING) as conn:
      # creamos un cursor para ejecutar comandos SQL
      return {
        "challenges": [
          {"id": id, "title": title, "description": description}
          for id, title, description in fetch_all_challenges(conn)
        ]
      }
  except Exception as e:
    # manejo de errores
    print(f"Error al obtener todos los retos: {e}")


# Ruta para obtener un reto aleatorio
@router.get("/get_aleatory_challenge")
async def get_challenge_by_id():
  # manejo de errores
  try:
    # abrimos una conexión a la db
    with psycopg.connect(CONN_STRING) as conn:
      # creamos un cursor para ejecutar comandos SQL
      id, title, description = fetch_random_challenge(conn)
      return {"challenge": {id, title, description}}
  except Exception as e:
    # manejo de errores
    print(f"Erro al obtener un elemento aleatorio de la tabla retos: {e}")


# Ruta para crear un nuevo reto
@router.post("/create_challenge")
async def create_challenge(title: str, description: str):
  # manejo de errores
  try:
    # validamos los datos de entrada
    if not title or not description:
      # si faltan datos, lanzamos un error
      raise ValueError({"error": "El título y la descripción son obligatorios"})
    # abrimos una conexión a la db
    with psycopg.connect(CONN_STRING) as conn:
      # creamos un cursor para ejecutar comandos SQL
      insert_challenge(conn, title, description)
      return {"message": "Reto creado exitosamente"}
  except Exception as e:
    # manejo de errores
    print(f"Error al crear el reto: {e}")
