import os
from dotenv import load_dotenv


class Config:
    load_dotenv()
    SECRET_KEY = os.getenv('SECRET_KEY') or str(hash('N1lrin'))  # получение секретного ключа
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # получение ссылки на датабазу
    SQLALCHEMY_TRACK_MODIFICATIONS = False
