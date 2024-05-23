# Настройки проекта
import os
from dotenv import load_dotenv


class Config:
    load_dotenv()  # подгружаем данные из .env
    SECRET_KEY = os.getenv('SECRET_KEY') or str(hash('N1lrin'))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
