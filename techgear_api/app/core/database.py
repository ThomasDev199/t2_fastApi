
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.errors import PyMongoError

from app.core.config import settings
import certifi


# Conexión con MongoDB Atlas
client = MongoClient(
    settings.mongodb_uri,
    serverSelectionTimeoutMS=15000,
    connectTimeoutMS=15000,
    tlsCAFile=certifi.where()
)

# Base de datos
db: Database = client[settings.db_name]

# Colecciones
col_usuarios = db["usuarios"]
col_productos = db["productos"]
col_pedidos = db["pedidos"]


def init_indexes() -> None:
    """Crea los índices necesarios."""
    col_usuarios.create_index("email", unique=True)


def ping() -> None:
    """Comprueba la conexión con MongoDB."""
    client.admin.command("ping")


def close() -> None:
    """Cierra la conexión."""
    client.close()
