
from dotenv import load_dotenv
from os import getenv

load_dotenv()

database_url = getenv("DATABASE_URL")

TORTOISE_ORM = {
    "connections": {
        "default":database_url
    },
    "apps": {
        "models": {
            "models": ["models.OrdensProducao"],
            "default_connection": "default",
        }
    }
}
