from flask_restplus import fields
from web_app.api.restplus import api

response_body = api.model("response_body", {
    "response_msg": fields.String(required=True, description="response message"),
    "response_data": fields.Raw()
})

task = api.model("task", {
    "id": fields.Integer(readOnly=True, required=True, description="The unique identifier of a task"),
    "name": fields.String(required=True, description="Task name"),
})


tasks_response_body = api.inherit("tasks_response_body", response_body, {
    "response_data": fields.List(fields.Nested(task))
})


a_task_response_body = api.inherit("a_task_response_body", response_body, {
    "response_data": fields.Nested(task)
})
