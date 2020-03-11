from http import HTTPStatus
from unittest import TestCase
from mock import patch
from web_app.app import create_app


class TestTaskApi(TestCase):
    def setUp(self):
        app = create_app(testing=True)
        self.client = app.test_client()
        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    @patch("web_app.database.task_db.get_tasks")
    def test_get_tasks_with_empty_tasks(self, mock_get_tasks):
        empty_tasks = []
        mock_get_tasks.return_value = empty_tasks
        response = self.client.get("/api/tasks")
        self.assertEquals(HTTPStatus.OK.value, response.status_code)
        response_json = response.json
        response_data = response_json["response_data"]
        response_msg = response_json["response_msg"]
        self.assertListEqual(empty_tasks, response_data)
        self.assertEquals("success", response_msg)

    @patch("web_app.database.task_db.get_tasks")
    def test_get_tasks_with_two_tasks(self, mock_get_tasks):
        two_tasks = [{
            "id": 1,
            "name": "task_1"
        }, {
            "id": 2,
            "name": "task_2"
        }]
        mock_get_tasks.return_value = two_tasks
        response = self.client.get("/api/tasks")
        self.assertEquals(HTTPStatus.OK.value, response.status_code)
        response_json = response.json
        response_data = response_json["response_data"]
        response_msg = response_json["response_msg"]
        self.assertListEqual(two_tasks, response_data)
        self.assertEquals("success", response_msg)

    @patch("web_app.database.task_db.get_task_by_id")
    def test_get_a_task_when_task_not_found(self, mock_get_task_by_id):
        not_exist_task_id = 99999
        mock_get_task_by_id.return_value = None
        response = self.client.get(f"/api/tasks/{not_exist_task_id}")
        self.assertEquals(HTTPStatus.NOT_FOUND.value, response.status_code)
        response_json = response.json
        response_data = response_json["response_data"]
        response_msg = response_json["response_msg"]
        self.assertIsNone(response_data)
        self.assertEquals("Task not found", response_msg)

    @patch("web_app.database.task_db.get_task_by_id")
    def test_get_a_task(self, mock_get_task_by_id):
        task_id = 1
        a_task = {
            "id": task_id,
            "name": "task_1"
        }
        mock_get_task_by_id.return_value = a_task
        response = self.client.get(f"/api/tasks/{task_id}")
        self.assertEquals(HTTPStatus.OK.value, response.status_code)
        response_json = response.json
        response_data = response_json["response_data"]
        response_msg = response_json["response_msg"]
        self.assertDictEqual(a_task, response_data)
        self.assertEquals("success", response_msg)
