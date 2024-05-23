from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Создание модели для таблицы в MySQL
class TableTasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # первичный ключ айди, который создается сам
    title = db.Column(db.String(120), nullable=False)  # название задачи, не пустое значение
    description = db.Column(db.String(120), nullable=True)  # описание задачи, может быть пустым
    created_at = db.Column(db.DateTime, default=datetime.utcnow())  # дата создания приложения
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())  # обновляется дата

    def to_json(self):  # преобразование данных в json
        return {"id": self.id,
                "title": self.title,
                "description": self.description,
                "created_at": self.created_at,
                "updated_at": self.updated_at}
