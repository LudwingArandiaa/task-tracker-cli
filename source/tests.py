import unittest
import os
import json
from unittest.mock import patch

# Import the modules to test
from cli.models.managers import json_manager, file_manager

# Create a path to a tasks_test.json for the tests
TEST_JSON_PATH = file_manager.get_absolute_path_from_relative_path('tasks/tasks_test.json')


"""
    This class ensure the tests for the application
"""
class TestTaskJsonManager(unittest.TestCase):

    """
        This method setup the initial configuration for each test case
    """
    def setUp(self):
        print("Preparing test environment.")
        # Ensure the test file exists and is empty
        os.makedirs(os.path.dirname(TEST_JSON_PATH), exist_ok=True)
        # Create the tasks test json file for test the application
        with open(TEST_JSON_PATH, 'w') as f:
            json.dump([], f)

        # Patch the ABSOLUTE_PATH_TASK_JSON_FILE to use the test file
        patcher = patch('cli.models.managers.json_manager.ABSOLUTE_PATH_TASK_JSON_FILE', TEST_JSON_PATH)
        self.addCleanup(patcher.stop)
        self.mock_path = patcher.start()

    """
        This method tear down the configuration when the test finished
    """
    def tearDown(self):
        print("Tear down test environment.")
        # Remove the test file after each test
        if os.path.exists(TEST_JSON_PATH):
            os.remove(TEST_JSON_PATH)

    """
        Method for testing add a task in the json file evaluating the
        attributes of the task created
    """
    def test_add_task(self):
        print("\nTesting add task.")
        json_manager.write_task_json('Test Task', 'Test Description')
        print("\nInput: task-tracker add 'Test Task' 'Test Description'")
        tasks = json_manager.get_tasks_json_file_content()
        print(f"\nOutput: \n{len(tasks)} == 1\n'{tasks[0]['title']}' == 'Test Task'\n'{tasks[0]['description']}' == 'Task Description'")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]['title'], 'Test Task')
        self.assertEqual(tasks[0]['description'], 'Test Description')
        print("✅ \n\n")

    """
        Method for testing update a task in the json file with
        description and title by id
    """
    def test_update_task(self):
        print("Testing update task.")
        json_manager.write_task_json('Task', 'Desc')
        json_manager.update_task_json(0, 'title', 'Updated Task')
        print("\nInput:\ntask-tracker add 'Task' 'Desk'")
        print("task-tracker update '0' 'title' 'Updated Task'")
        tasks = json_manager.get_tasks_json_file_content()
        print(f"\nOutput: \n{tasks[0]['title']} == 'Updated Task'")
        self.assertEqual(tasks[0]['title'], 'Updated Task')
        print("✅ \n\n")

    """
        Method for testing delete a task in the json file by id
    """
    def test_delete_task(self):
        print("Testing delete task by id.")
        json_manager.write_task_json('Task', 'Desc')
        json_manager.delete_task_json(0)
        print("\nInput:\ntask-tracker add 'Task' 'Desc'\ntask-tracker delete '0'")
        tasks = json_manager.get_tasks_json_file_content()
        print(f"Output:\n{len(tasks)} == 0")
        self.assertEqual(len(tasks), 0)
        print("✅ \n\n")
    
    """
        Method for testing filter tasks by argument
    """
    def test_filter_tasks_by_argument(self):
        print("Testing filter tasks by argument")
        json_manager.write_task_json('Task1', 'Desc1')
        json_manager.write_task_json('Task2', 'Desc2')
        json_manager.update_task_json(1, 'state', 'Done')
        print("\nInput:\ntask-tracker add 'Task1' 'Desc1'\ntask-tracker add 'Task2' Desc2'\ntask-tracker mark-done '1'")
        done_tasks = json_manager.filter_tasks_by_argument('Done')
        print(f"Output:\n{len(done_tasks)} == 1\n{done_tasks[0]['title']} == 'Task2")
        self.assertEqual(len(done_tasks), 1)
        self.assertEqual(done_tasks[0]['title'], 'Task2')
        print("✅ \n\n")

if __name__ == '__main__':
    unittest.main()