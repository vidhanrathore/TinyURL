import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DB = os.getenv('MYSQL_DB')
MYSQL_PORT = os.getenv('MYSQL_PORT')


DB_CONFIG = {
    "host": MYSQL_HOST,
    "port": 28271,
    "user": MYSQL_USER,
    "password": MYSQL_PASSWORD,
    "db": MYSQL_DB,
    "charset": "utf8mb4",
    "cursorclass": "DictCursor",
    "connect_timeout": 10,
    "read_timeout": 10,
    "write_timeout": 10,
}

