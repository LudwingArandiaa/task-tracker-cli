from datetime import datetime as dt
import os

str_datetime_now = lambda: str(dt.now())

def get_absolute_path_from_relative_path(relative_path):
    def get_actual_path():
        return os.path.dirname(os.path.abspath(__file__))
    
    return os.path.join(get_actual_path(), relative_path)
    
def create_dir_if_not_exit_in_relative_path(dir_relative_path):
    dir_absolute_path = get_absolute_path_from_relative_path(dir_relative_path)
    return os.makedirs(os.path.dirname(dir_absolute_path), exist_ok=True)

def create_task_content(task_id, task_title, task_description=''):
    return {
        'id': task_id,
        'title': task_title,
        'state': 'To do',
        'description': task_description,
        'createdAt': str_datetime_now(),
        'updatedAt': str_datetime_now(),
    }

def search_task_content(tasks_list, task_id):
    for task in tasks_list:
        if task['id'] == int(task_id):
            return task
    return None

def put_task_in_content(task_to_put, task_content):
    for idx, task in enumerate(task_content):
        if task.get('id') == task_to_put.get('id'):
            task_content[idx] = task_to_put
            break
    return task_content

def remove_task_object_from_id(task_id, task_content):
    for task in task_content:
        if task['id'] == int(task_id):
            task_content.pop(int(task_id))
    new_task_content = [{'id' : new_id, **attribute} for new_id, attribute in enumerate(task_content)]
    return new_task_content