import shutil
import pydoc
import os

# Output directory for the documentation
output_dir = 'doc'

# List all of the modules for document in the project
modules_to_document = [
    'source.task_tracker'
]

# Create the doc directory if not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create the documentation for each module
for module_name in modules_to_document:
    # Generate the documentation for the iterable module
    pydoc.writedoc(module_name)
    html_file = f"{module_name}.html"
    # Move the html file to the directory
    if os.path.exists(html_file):
        shutil.move(html_file, os.path.join(output_dir, html_file))
        print(f"Documentation for '{module_name}.py' generated in '{os.path.join(output_dir, html_file)}'.")
    else:
        print(f"Couldn't generate html file for '{module_name}.py'")

print("Documentation process finished.")