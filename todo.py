"""Todo application."""

import sys


def read_file():
    """Function to open and read file with tasks list."""
    tasks_list = []
    with open("todo.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            tasks_list.append(line)
    return tasks_list


def list_items():
    """List all tasks."""
    tasks = read_file()
    if len(tasks) == 0:
        print("No todos for today! :)")
    if len(tasks) > 0:
        for idx, item in enumerate(tasks):
            sys.stdout.buffer.write(
                f"{idx+1} - {item}".encode("utf8"))
            sys.stdout.buffer.write("\n".encode("utf8"))


def info():
    """Prints usage functions of todo list."""
    text = (
        """Command Line Todo application
=============================

Command line arguments:
-l   Lists all the tasks
-a   Adds a new task
-r   Removes an task
-c   Completes an task""")
    sys.stdout.buffer.write(text.encode("utf8"))


if __name__ == "__main__":
    args = sys.argv
    try:
        if args[0] == "todo.py":
            if len(args) == 1:
                globals()["info"]()
            if args[1] == "-l":
                args[1] = "list_items"
                globals()[args[1]]()
    except IndexError:
        pass
