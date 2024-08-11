from flask import Flask
from app.routes import init_routes
import os
from dotenv import load_dotenv

# Memuat file .env
load_dotenv()

# Mengambil nilai dari .env
FLASK_ENV = os.getenv('FLASK_ENV')
FLASK_RUN_PORT = os.getenv('FLASK_RUN_PORT', 5000)  # Default port 5000 jika tidak ada dalam .env

app = Flask(__name__)

# Menentukan konfigurasi berdasarkan lingkungan
app.config['ENV'] = FLASK_ENV
app.config['DEBUG'] = os.getenv('DEBUG', 'True').lower() == 'true'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Inisialisasi route
init_routes(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(FLASK_RUN_PORT))
