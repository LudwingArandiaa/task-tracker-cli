from .managers import json_manager
from datetime import datetime

class Tasks():
    def __init__(self, title, description):
        self.id = len(json_manager.get_tasks_json_file_content())
        self.title = title
        self.state = 'To do'
        self.description = description
        self.createdAt = datetime.now()
        self.updateAt = datetime.now()

    def create(self):
        json_manager.write_task_json(self.title, self.description)

    @staticmethod
    def read():
        return json_manager.get_tasks_json_file_content()

    @staticmethod
    def update(task_id, task_attribute, task_new_value):
        json_manager.update_task_json(task_id, task_attribute, task_new_value)

    @staticmethod
    def delete(task_id):
        json_manager.delete_task_json(task_id)

    @staticmethod
    def filter(tasks_state):
        return json_manager.filter_tasks_by_argument(tasks_state)
    
    @staticmethod
    def get_tasks_in_list(tasks):
            return [f"{index + 1}. {task.get('title', 'Untitled')}: {task.get('description', 'No description')}. ({task.get('state', 'Unknown')})" for index, task in enumerate(tasks)]