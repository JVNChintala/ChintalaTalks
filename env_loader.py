import os

from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("BASE_URL", None)
api_key = os.getenv("API_KEY", None)
model = os.getenv("MODEL", "gpt-4o")
