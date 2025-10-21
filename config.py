import os
from dotenv import load_dotenv

# Membaca file .env di root project
load_dotenv()

# Lokasi dasar project
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Mengambil secret key dari .env, default "super_secret_key" jika tidak ada
    SECRET_KEY = os.getenv("SECRET_KEY", "super_secret_key")

    # Mengambil database URI dari .env, default sqlite
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{os.path.join(BASE_DIR, 'company.db')}"
    )

    # Mengambil track modifications, default False
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", "False").lower() == "true"
    )

    # Mode environment (development / production)
    FLASK_ENV = os.getenv("FLASK_ENV", "development")