import os
from pathlib import Path
from dotenv import load_dotenv

APP_DIR = Path(__file__).resolve()
load_dotenv(dotenv_path=APP_DIR / "local.env")

# Now you can access your environment variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

# Example usage
print("Database Host:", db_host)
print("Database User:", db_user)
