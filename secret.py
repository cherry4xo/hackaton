from decouple import config

API_TOKEN = config("API_TOKEN", cast=str)
