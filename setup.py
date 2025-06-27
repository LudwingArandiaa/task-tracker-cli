from setuptools import setup

setup(
    name="task-tracker",
    version="1.0",
    py_modules=["source.task_tracker"],
    entry_points={
        "console_scripts": [
            "task-tracker=source.task_tracker:main"
        ]
    },
)