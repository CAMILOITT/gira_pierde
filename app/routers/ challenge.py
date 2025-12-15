import os

import psycopg
from dotenv import load_dotenv
from fastapi import APIRouter

load_dotenv()  # Carga las variables de entorno desde el archivo .env
router = APIRouter(prefix="/challenge", tags=["challenge"])


@router.get("/all_get_challenge")
async def get_challenge():
  return {"ok": True}
  pass
  # try:
  #   conn_string = os.getenv("DATABASE_URL")
  #   with psycopg.connect(conn_string) as conn:
  #     with conn.cursor() as cur:
  #       cur.execute("SELECT * FROM challenges;")
  #       challenges = cur.fetchall()
  #       return {"challenges": challenges}
  # except Exception as e:
  #   print(f"Error retrieving challenges: {e}")


@router.get("/get_aleatory_challenge")
async def get_challenge_by_id():
  return {"ok": True}
  pass
  # try:
  #   conn_string = os.getenv("DATABASE_URL")
  #   # with psycopg.connect(conn_string) as conn:
  #   #   with conn.cursor() as cur:
  #   #     cur.execute("SELECT * FROM challenges ORDER BY RANDOM() LIMIT 1;")
  #   #     challenge = cur.fetchone()
  #   #     return {"challenge": challenge}
  # except Exception as e:
  #   print(f"Error retrieving aleatory challenge: {e}")
