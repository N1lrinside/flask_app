from views import TaskListResources, TaskResource
from flask import Api
from app import app

api = Api()
api.add_resource(TaskListResources, "/tasks")
api.add_resource(TaskResource, '/tasks/<int:task_id>')
api.init_app(app)


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        print('Exit')

