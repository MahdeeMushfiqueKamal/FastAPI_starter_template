import os
from dotenv import load_dotenv

load_dotenv()

# Now you can access your environment variables
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
