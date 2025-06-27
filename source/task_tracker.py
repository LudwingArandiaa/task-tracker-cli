#!/usr/bin/env python3
from .cli.interface import Task_tracker
from .cli.commands import command_map


"""
    This is the main function.
    If the commands arguments of the program are in the command map
    The cli will execute the function that the arguments said in the call
    of the program.
"""
def main():
    program = Task_tracker()
    if program.arguments.command in command_map:
        command_map[program.arguments.command](program.arguments)
    else:
        print(f"Unknown command: {program.arguments.command}. Use --help to see available commands.")

if __name__ == '__main__':
    main()