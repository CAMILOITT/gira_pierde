import os

import psycopg
from dotenv import load_dotenv
from fastapi import APIRouter

load_dotenv()  # Carga las variables de entorno desde el archivo .env
router = APIRouter(prefix="/challenge", tags=["challenge"])


@router.get("/get_all_challenge")
async def get_challenge():
  try:
    conn_string = os.getenv("DATABASE_URL")
    with psycopg.connect(conn_string) as conn:
      with conn.cursor() as cur:
        cur.execute("SELECT * FROM challenges;")
        challenges = cur.fetchall()
        return {
          "challenges": [
            {"id": id, "title": title, "description": description}
            for id, title, description in challenges
          ]
        }
  except Exception as e:
    print(f"Error retrieving challenges: {e}")


@router.get("/get_aleatory_challenge")
async def get_challenge_by_id():
  try:
    conn_string = os.getenv("DATABASE_URL")
    with psycopg.connect(conn_string) as conn:
      with conn.cursor() as cur:
        cur.execute("SELECT * FROM challenges ORDER BY RANDOM() LIMIT 1;")
        id, name, description = cur.fetchone()
        return {"challenge": {"id": id, "name": name, "description": description}}
  except Exception as e:
    print(f"Error retrieving aleatory challenge: {e}")


@router.post("/create_challenge")
async def create_challenge(title: str, description: str):
  try:
    conn_string = os.getenv("DATABASE_URL")
    with psycopg.connect(conn_string) as conn:
      with conn.cursor() as cur:
        cur.execute(
          "INSERT INTO challenges (title, description) VALUES (%s, %s) RETURNING id;",
          (title, description),
        )
        new_id = cur.fetchone()[0]
        conn.commit()
        return {"message": "Challenge created successfully", "id": new_id}
  except Exception as e:
    print(f"Error creating challenge: {e}")
