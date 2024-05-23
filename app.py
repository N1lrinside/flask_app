# Импорт библиотек и приложения
from app.views import TaskListResources, TaskResource
from flask_restful import Api
from app import app

# Создание Api
api = Api()
# Регистрируем методы и присваем определенным ссылкам
api.add_resource(TaskListResources, "/tasks")
api.add_resource(TaskResource, '/tasks/<int:task_id>')
# Инициализируем проект
api.init_app(app)

# Запуск проекта
if __name__ == '__main__':
    app.run(debug=True)
