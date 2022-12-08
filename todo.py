"""Todo application."""

import sys


def read_file():
    """Function to open and read file with tasks list.
    Returns - list - tasks outline."""
    tasks_list = []
    with open("todo.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip("\n")
            tasks_list.append(line)
    return tasks_list


def list_items():
    """List all tasks.
    If there is no tasks prints message."""
    tasks = read_file()
    if len(tasks) == 0:
        print("No todos for today! :)")
    if len(tasks) > 0:
        for idx, item in enumerate(tasks):
            sys.stdout.buffer.write(
                f"{idx+1} - {item}".encode("utf8"))
            sys.stdout.buffer.write("\n".encode("utf8"))


def add_task(new_tasks):
    """Function for adding task to the todo.txt.
    Argument - str - task."""
    with open("todo.txt", "a", encoding="utf-8") as file:
        for idx_t in new_tasks:
            file.write(idx_t)
            file.write("\n")


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
            elif args[1] == "-l":
                args[1] = "list_items"
                globals()[args[1]]()
            elif args[1] == "-a":
                args[1] = "add_task"
                if len(args) < 3:
                    print("Unable to add: no task provided")
                else:
                    globals()[args[1]](args[2:])

    except IndexError:
        pass
