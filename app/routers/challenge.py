# Importamos la librería para conectarnos a Postgres
import psycopg
from dotenv import load_dotenv
from fastapi import APIRouter

# Importamos la cadena de conexión desde las constantes
from app.const import CONN_STRING

load_dotenv()  # Carga las variables de entorno desde el archivo .env

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
      with conn.cursor() as cur:
        # ejecutamos el comando SQL para obtener todos los retos
        cur.execute("SELECT * FROM challenges;")
        # obtenemos todos los retos
        challenges = cur.fetchall()
        # devolvemos los retos en formato JSON
        return {
          "challenges": [
            {"id": id, "title": title, "description": description}
            for id, title, description in challenges
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
      with conn.cursor() as cur:
        # ejecutamos el comando SQL para obtener todos los retos
        cur.execute("SELECT * FROM challenges ORDER BY RANDOM() LIMIT 1;")
        id, name, description = cur.fetchone()
        # retornamos los datos al cliente en formato JSON
        return {"challenge": {"id": id, "name": name, "description": description}}
  except Exception as e:
    # manejo de errores
    print(f"Erro al obtener un elemento aleatorio de la tabla retos: {e}")


# Ruta para crear un nuevo reto
@router.post("/create_challenge")
async def create_challenge(title: str, description: str):
  # manejo de errores
  try:
    # abrimos una conexión a la db
    with psycopg.connect(CONN_STRING) as conn:
      # creamos un cursor para ejecutar comandos SQL
      with conn.cursor() as cur:
        # ejecutamos el comando SQL para obtener todos los retos
        cur.execute(
          "INSERT INTO challenges (title, description) VALUES (%s, %s) RETURNING id;",
          (title, description),
        )
        # obtenemos el id del nuevo reto
        new_id = cur.fetchone()[0]
        # confirmamos los cambios en la db
        conn.commit()
        # retornamos los datos al cliente en formato JSON
        return {"message": "El reto fue creado satisfactoriamente", "id": new_id}
  except Exception as e:
    # manejo de errores
    print(f"Error al crear el reto: {e}")
