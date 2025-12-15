# Importamos las librerías necesarias para nuestra practica
import os

from dotenv import load_dotenv
from fastapi import FastAPI

from app.routers.challenge import router

load_dotenv()  # Carga las variables de entorno desde el archivo .env

conn_string = os.getenv("DATABASE_URL")

print(conn_string)
# Inicializamos la aplicación FastAPI
app = FastAPI()


app.include_router(router)
