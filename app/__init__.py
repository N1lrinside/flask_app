from flask import Flask
from config import Config
from app.models import db

app = Flask(__name__)  # Создание Flask приложения
app.config.from_object(Config)  # Настройка конфигурации приложения
db.init_app(app)  # инициализируем базу данных в приложение

# Создание таблицы базы данных
with app.app_context():
    db.create_all()
