# importamos librerías
import json
from typing import Any, Dict

# definimos la ruta del archivo JSON
FILE_PATH = "data.json"

# funciones para leer y escribir en el archivo JSON
def read() -> Dict[str, Any]:
  # leemos el archivo JSON
  with open(FILE_PATH, "r", encoding="utf-8") as f:
    return json.load(f)


# función privada para escribir en el archivo JSON
def write(data: Dict[str, Any]) -> None:
  # escribimos en el archivo JSON
  with open(FILE_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)


# función para subir datos desde un archivo JSON
def upload(json_path: str) -> None:
  try:
    # leemos el archivo JSON proporcionado
    with open(json_path, "r", encoding="utf-8") as f:
      data = json.load(f)
    write(data)
  except ErrorValue as err:
    print(err)
    print("No se pudo leer el archivo")


# función para descargar datos del archivo JSON
def download() -> Dict[str, Any]:
  return read()


# función para actualizar datos en el archivo JSON
def update_data(payload: Dict[str, Any]) -> None:
  data = read()
  update(payload)
  write(data)
