from http import HTTPStatus
from flask_restplus import Resource
from web_app.api.restplus import api
from web_app.api.task import serializers
from web_app.service import task_service


tasks_namespace = api.namespace("tasks", description="tasks operation")


@tasks_namespace.route("")
class TaskCollection(Resource):

    @api.marshal_with(serializers.tasks_response_body)
    def get(self):
        """
        Returns list of tasks.
        """

        return task_service.get_tasks()


@tasks_namespace.route("/<int:task_id>")
@api.response(HTTPStatus.NOT_FOUND.value, "Task not found")
class TaskItem(Resource):

    @api.marshal_with(serializers.a_task_response_body)
    def get(self, task_id):
        """
        Returns a task
        """

        return task_service.get_task_by_id(task_id=task_id)