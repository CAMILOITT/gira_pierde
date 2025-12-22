from psycopg import Connection


# obtención de todos los desafíos.
def fetch_all_challenges(conn: Connection) -> list:
  """
  Obtiene todos los desafíos de la base de datos.

  **Args**:
    conn (Connection): Conexión a la base de datos.

  **Returns**:
    list: Lista de todos los desafíos.
  """
  # creación de un cursor para ejecutar comandos SQL
  with conn.cursor() as cur:
    # ejecuta el comando SQL para obtener todos los retos
    cur.execute("SELECT * FROM challenges;")
    return cur.fetchall()


# obtención de un desafío aleatorio.
def fetch_random_challenge(conn: Connection) -> tuple:
  # docstring
  """
  Obtiene un desafío aleatorio de la base de datos.

  **Args**:
    conn (Connection): Conexión a la base de datos.

  **Returns**:
    tuple: Desafío aleatorio. (ID, título, descripción)
  """
  # creación de un cursor para ejecutar comandos SQL
  with conn.cursor() as cur:
    # ejecuta el comando SQL para obtener todos los retos
    cur.execute("SELECT * FROM challenges ORDER BY RANDOM() LIMIT 1;")
    return cur.fetchone()


# creación de un nuevo desafío.
def insert_challenge(conn: Connection, title: str, description: str) -> int:
  """
  Crea un nuevo desafío en la base de datos.

  **Args**:
    conn (Connection): Conexión a la base de datos.
    title (str): Título del desafío.
    description (str): Descripción del desafío.

  **Returns**:
    int: ID del nuevo desafío creado.
  """
  # creación de un cursor para ejecutar comandos SQL
  with conn.cursor() as cur:
    # ejecuta el comando SQL para obtener todos los retos
    cur.execute(
      "INSERT INTO challenges (title, description) VALUES (%s, %s) RETURNING id;",
      (title, description),
    )
    return cur.fetchone()[0]


# eliminación de un desafío por su ID.
def delete_challenge(conn: Connection, challenge_id: int) -> None:
  """
  Elimina un desafío de la base de datos por su ID.
  **Args**:
    conn (Connection): Conexión a la base de datos.
    challenge_id (int): ID del desafío a eliminar.
  """
  # creación de un cursor para ejecutar comandos SQL
  with conn.cursor() as cur:
    # ejecuta el comando SQL para obtener todos los retos
    cur.execute(
      "DELETE FROM challenges WHERE id = %s;",
      (challenge_id,),
    )
