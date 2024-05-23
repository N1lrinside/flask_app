from flask import jsonify, abort, request, Response
from app.models import db, TableTasks
from flask_restful import Resource
from sqlalchemy import text, exc


# Для работы со всеми задачами
class TaskListResources(Resource):

    def get(self) -> Response:
        """get tasks"""
        tasks = TableTasks.query.all()
        return jsonify([task.to_json() for task in tasks])

    def post(self) -> Response:
        """create task"""
        data = request.get_json()

        if "title" not in data:
            return {"message": "Название отсутствует"}, 400

        if not isinstance(data["title"], str):
            return {"message": "Недоступный тип данных для названия"}, 400

        if data.get("description"):
            if not isinstance(data["description"], str):
                return {"message": "Недоступный тип данных для описания"}, 400

        new_task = TableTasks(title=data['title'], description=data.get('description'))
        try:
            db.session.add(new_task)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description=f"Ошибка базы данных: {e}")
        return jsonify(new_task.to_json())


class TaskResource(Resource):

    def get(self, task_id: int) -> Response:
        """get task by task_id"""
        task = TableTasks.query.get_or_404(task_id)
        return jsonify(task.to_json())

    def put(self, task_id: int) -> Response:
        """update task by task_id"""
        task = TableTasks.query.get_or_404(task_id)
        data = request.get_json()
        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        try:
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description=f"Ошибка базы данных: {e}")
        return jsonify(task.to_json())

    def delete(self, task_id: int) -> Response:
        """delete task by task_id"""
        task = TableTasks.query.get_or_404(task_id)
        try:
            db.session.delete(task)
            db.session.commit()
            db.session.execute(text("ALTER TABLE table_tasks AUTO_INCREMENT = 1"))
            db.session.commit()
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            abort(500, description=f"Ошибка базы данных: {e}")
        return "Задача успешно удалена"
