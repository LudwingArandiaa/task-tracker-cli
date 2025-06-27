from .models.tasks import Tasks

TASK_TITLE_ARGUMENT_NAME = 'title'
TASK_DESCRIPTION_ARGUMENT_NAME = 'description'
TASK_STATE_ARGUMENT_NAME = 'state'

def add_task(task_title, task_description=''):
    task = Tasks(title=task_title, description=task_description)
    task.create()

def delete_task(task_id):
    Tasks.delete(task_id)

def update_task(task_id, task_new_title=None, task_new_description=None, task_new_state=None):
    if task_new_description is None and task_new_title is None and task_new_state is None:
        raise Exception('Neither title nor description has been received')
    if task_new_title is not None:
        Tasks.update(task_id, TASK_TITLE_ARGUMENT_NAME, task_new_title)
    if task_new_description is not None:
        Tasks.update(task_id, TASK_DESCRIPTION_ARGUMENT_NAME, task_new_description)
    if task_new_state is not None:
        Tasks.update(task_id, TASK_STATE_ARGUMENT_NAME, task_new_state)

def watchout_tasks(tasks_state=None):
    if tasks_state is None: tasks = Tasks.read()
    else: tasks = Tasks.filter(tasks_state)
    tasks_list = Tasks.get_tasks_in_list(tasks)
    for element_task_in_list in tasks_list:
        print(element_task_in_list) 