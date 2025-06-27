from . import tasks_controller


command_map = {
    "add": lambda args: tasks_controller.add_task(task_title=args.title, task_description=args.description),
    "update": lambda args: tasks_controller.update_task(task_id=str(args.id), task_new_title=args.title, task_new_description=args.description),
    "delete": lambda args: tasks_controller.delete_task(str(args.id)),
    "mark-in-progress": lambda args: tasks_controller.update_task(str(args.id), task_new_state='In progress'), 
    "mark-done": lambda args: tasks_controller.update_task(str(args.id), task_new_state='Done'),
    "list": lambda _: tasks_controller.watchout_tasks(),
    "list-to-do": lambda _: tasks_controller.watchout_tasks('To do'),
    "list-in-progress": lambda _: tasks_controller.watchout_tasks('In progress'),
    "list-done": lambda _: tasks_controller.watchout_tasks('Done'),
}