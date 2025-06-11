from dotenv import load_dotenv
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, '.env'))

MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
if not MONGO_PASSWORD:
    raise ValueError("MONGO_PASSWORD is not set in the environment variables or .env file.")
SECRET_KEY = os.getenv('SECRET_KEY')

MONGO_URL = f"mongodb+srv://yingOuOb:{MONGO_PASSWORD}@cluster0.l83fzgt.mongodb.net/OuOb?retryWrites=true&w=majority&appName=Cluster0"

class Config(object):
    MONGO_URI=MONGO_URL
    SECRET_KEY = SECRET_KEY
#不要再把URI寫成URL了 >:(