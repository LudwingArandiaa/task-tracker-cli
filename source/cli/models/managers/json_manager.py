from datetime import datetime as dt
from . import file_manager
import json
import os

VOID_LIST = []
ABSOLUTE_PATH_TASK_JSON_FILE = file_manager.get_absolute_path_from_relative_path('tasks/tasks.json')
TASK_DIR = 'tasks/'

WRITE = 'w'
READ = 'r'

def tasks_json_file_exist():
    return os.path.isfile(ABSOLUTE_PATH_TASK_JSON_FILE)

def create_tasks_json_file():
    file_manager.create_dir_if_not_exit_in_relative_path(TASK_DIR)
    with open(ABSOLUTE_PATH_TASK_JSON_FILE, WRITE) as tasks_file:
        json.dump(VOID_LIST, tasks_file)

def evaluate_if_tasks_files_exists(function):
    def wrapper(*args, **kwargs):
        if not tasks_json_file_exist():
            create_tasks_json_file()
        return function(*args, **kwargs)
    return wrapper

@evaluate_if_tasks_files_exists
def get_tasks_json_file_content():
    with open(ABSOLUTE_PATH_TASK_JSON_FILE, READ) as tasks_file:
        return json.load(tasks_file)

@evaluate_if_tasks_files_exists
def write_task_json(new_task_title, new_task_description=''):
    json_data = get_tasks_json_file_content()
    TASKS_QUANTITY = len(json_data)

    new_task = file_manager.create_task_content(task_title=new_task_title, task_description=new_task_description, task_id=TASKS_QUANTITY)
    json_data.append(new_task)
    with open(ABSOLUTE_PATH_TASK_JSON_FILE, WRITE) as tasks_file:
        json.dump(json_data, tasks_file)
    print("Task added successfully!")

@evaluate_if_tasks_files_exists
def update_task_json(task_id, task_attribute, task_new_value):
    tasks_content = get_tasks_json_file_content()
    task_to_update = file_manager.search_task_content(tasks_content, task_id)
    if task_to_update is None:
        print(f"Task with id={task_id} doesn't")
        return
    task_to_update[task_attribute] = task_new_value
    task_to_update['updatedAt'] = str(dt.now())
    json_data_with_task_updated = file_manager.put_task_in_content(task_to_update, tasks_content)
    with open(ABSOLUTE_PATH_TASK_JSON_FILE, WRITE) as tasks_file:
        json.dump(json_data_with_task_updated, tasks_file)
    print(f"Task {task_attribute} updated successfully!")

@evaluate_if_tasks_files_exists
def delete_task_json(task_id):
    tasks_content = get_tasks_json_file_content()
    try:
        json_data_with_task_deleted = file_manager.remove_task_object_from_id(task_id, tasks_content)
    except:
        print(f"The id={task_id} doesn't")
        return
    
    with open(ABSOLUTE_PATH_TASK_JSON_FILE, WRITE) as tasks_file:
        json.dump(json_data_with_task_deleted, tasks_file)
    print("Task deleted successfully!")

def filter_tasks_by_argument(tasks_state):
    tasks_content = get_tasks_json_file_content()
    return [task for task in tasks_content if task['state'] == tasks_state]