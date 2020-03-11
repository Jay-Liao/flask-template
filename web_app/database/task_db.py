def get_tasks():
    tasks = [{
        "id": 1,
        "name": "task_1"
    }]
    return tasks


def get_task_by_id(task_id):
    task_map = {
        1: {
            "id": 1,
            "name": "task_1"
        },
        2: {
            "id": 2,
            "name": "task_2"
        },
        3: {
            "id": 3,
            "name": "task_3"
        }
    }
    task = task_map.get(task_id, None)
    return task
