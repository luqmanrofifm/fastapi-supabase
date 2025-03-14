import os
from dotenv import load_dotenv

if os.environ.get("ENVIRONTMENT") != "prod":
    from dotenv import load_dotenv

    load_dotenv()


POSTGRESQL_USER = os.environ.get("POSTGRESQL_USER")
POSTGRESQL_PASSWORD = os.environ.get("POSTGRESQL_PASSWORD")
POSTGRESQL_HOST = os.environ.get("POSTGRESQL_HOST")
POSTGRESQL_PORT = os.environ.get("POSTGRESQL_PORT")
POSTGRESQL_DATABASE = os.environ.get("POSTGRESQL_DATABASE")
POSTRGESQL_POOL_SIZE = int(os.environ.get("POSTRGESQL_POOL_SIZE", "40"))