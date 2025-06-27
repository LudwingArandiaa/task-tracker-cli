#!/usr/bin/env python3
from source.cli.interface import Task_tracker
from source.cli.commands import command_map

def main():
    program = Task_tracker()
    if program.arguments.command in command_map:
        command_map[program.arguments.command](program.arguments)
    else:
        print(f"Unknown command: {program.arguments.command}. Use --help to see available commands.")

if __name__ == '__main__':
    main()