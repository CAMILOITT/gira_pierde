# importamos librerías
import json

from lib import download, update_data, upload


# menú interactivo simple
def menu() -> None:
  # bucle del menú
  while True:
    # mostramos las opciones
    print("\n1. Subir (ruta JSON)")
    print("2. Bajar (ver JSON)")
    print("3. Aumentar (añadir contenido)")
    print("4. Salir")

    # leemos la opción
    op = input("Opción: ").strip()

    if op == "1":
      # leemos la ruta del archivo JSON
      path = input("Ruta del archivo JSON: ")
      upload(path)

    elif op == "2":
      # mostramos el contenido del archivo JSON
      print(json.dumps(download(), indent=2, ensure_ascii=False))

    elif op == "3":
      # leemos la clave y el valor a añadir
      key = input("Ingrese la clave del json: ")
      # leemos el valor a añadir
      value = input("Ingrese el valor del json: ")
      # creamos un JSON temporal para actualizar
      raw = json.dumps({key: value})
      # actualizamos el archivo JSON
      update_data(json.loads(raw))

    elif op == "4":
      break


if __name__ == "__main__":
  menu()
