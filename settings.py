import os
from dotenv import load_dotenv

if os.environ.get("ENVIRONTMENT") != "prod":
    from dotenv import load_dotenv

    load_dotenv()
