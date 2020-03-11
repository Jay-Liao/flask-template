from http import HTTPStatus
from web_app.lib.response_factory import build_response
from web_app.database import task_db


def get_tasks():
    return build_response(response_data=task_db.get_tasks())


def get_task_by_id(task_id):
    task = task_db.get_task_by_id(task_id=task_id)
    if task is not None:
        return build_response(response_data=task)
    else:
        return build_response(response_msg="Task not found", status_code=HTTPStatus.NOT_FOUND.value)
