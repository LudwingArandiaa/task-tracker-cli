import argparse

class Task_tracker:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='task-cli', description='', usage='%(prog)s [option]', epilog='')
        self.command_line_interface = self.parser.add_subparsers(dest='command')

        self.add_task = self.command_line_interface.add_parser('add')
        self.add_task.add_argument('title', type=str)
        self.add_task.add_argument('description', type=str, default='')

        self.update_task = self.command_line_interface.add_parser('update')
        self.update_task.add_argument('id', type=str)
        self.update_task.add_argument('title', type=str)
        self.update_task.add_argument('description', type=str, default='')

        self.delete_task = self.command_line_interface.add_parser('delete')
        self.delete_task.add_argument('id', type=int)

        self.list_tasks = self.command_line_interface.add_parser('list')
        self.list_to_do = self.command_line_interface.add_parser('list-to-do')
        self.list_in_progress = self.command_line_interface.add_parser('list-in-progress')
        self.list_done = self.command_line_interface.add_parser('list-done')

        self.mark_in_progress = self.command_line_interface.add_parser('mark-in-progress')
        self.mark_in_progress.add_argument('id', type=int)

        self.mark_done = self.command_line_interface.add_parser('mark-done')
        self.mark_done.add_argument('id', type=int)

        self.arguments = self.parser.parse_args()