# 🗃️ Task Tracker Command Line Interface 
lightweight command-line application written in Python that allows you to manage your tasks efficiently. You can create, list, modify, and delete tasks, all stored in a simple JSON file.

## 📌 Features
* Create tasks with title and description
* Update task state with 'To do', 'Done' and 'In progress'
* Update task title and description by id
* List all the tasks and tasks by state (Done, To do, In progress)
* Delete task by id

## 🛠️ Prerequisites
* Python interpreter.
```bash
sudo apt-get install python
```
> Use apt installation in linux debian based distributions like Ubuntu, ZorinOS or MintOS.
> For Windows see the [python installation guide](https://www.python.org/)
* Git bash.
```bash
sudo apt-get install git
```
> Use apt installation in linux debian based distributions like Ubuntu, ZorinOS or MintOS.
> For Windows see the [python installation guide](https://git-scm.com/)
## ⚙️ Installation
### 1. Clone this repository:
```bash
git clone https://github.com/LudwingArandiaa/task-tracker-cli
```
### 2. Go to project directory:
```bash
cd task-tracker-cli
```
### 3. Install build dependencies:

1. Pip build libraries.
```bash
pip install build
```
2. Build the pip installer.
```bash
python -m build
```
3. Install program with pip.
```bash
pip install dist/task_tracker-1.0-py3-none-any.whl
```
4. Run the program.
```bash
task-tracker add 'My task' 'Do my homework'
```
## 📝 How to use

### ➕ Create task
You can use 'add' parser to create a task by using a title and description for the task like this:
```bash
task-tracker add 'My new task' 'description'
```
The task-tracker cli will automatically put the id and created date and updated date for each task added and modified. 
> NOTE: New task need to receives a title and a description arguments for to be created.

### 🟰 Update task
You can use 'update' parser to update a task title and the description by its id. You can do this like this:
```bash
task-tracker update '3' 'New title' 'New description'
```
> NOTE: The cli need to receives all of the arguments for update the task.

* Update task state.
    * You can update only a task state to **'In progress'** by its id with 'mark-in-progress': `task-tracker mark-in-progress '1'`.
    * You can update only a task state to **'Done'** by its id with 'mark-done': `task-tracker mark-done '1'`.
### ➗ List tasks
You can use **'list'** parser for show the list of tasks created in the json file. Only use the following script:
```bash
task-tracker list
```
* Filter by task state
    * Use **'list-to-do'** for show all the tasks with state 'To do': `task-tracker list-to-do`.
    * Use **'list-in-progress'** for show all the tasks with state 'In progress': `task-tracker list-in-progress`.
    * Use **'list-done'** for show all the tasks with state 'Done': `task-tracker list-done`.

### ➖ Delete task
You can use **'delete'** parser to delete a task by its id: `task-tracker delete '2'`.

## 📂 Project files directory
```
.
├── generate_docs.py
├── LICENSE
├── pyproject.toml
├── README.md
└── source
    ├── cli
    │   ├── commands.py
    │   ├── __init__.py
    │   ├── interface.py
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── managers
    │   │   │   ├── file_manager.py
    │   │   │   ├── __init__.py
    │   │   │   ├── json_manager.py
    │   │   │   └── tasks
    │   │   │       └── tasks.json
    │   │   └── tasks.py
    │   └── tasks_controller.py
    ├── __init__.py
    ├── task_tracker.py
    └── tests.py
```

## 📬 Contact
Let me know if you'd like any modifications! 🚀