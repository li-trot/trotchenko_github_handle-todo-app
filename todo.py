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
    """Lists all tasks.
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
    """Function for adding tasks to the todo.txt.
    Argument - list - task or list of tasks."""
    with open("todo.txt", "a", encoding="utf-8") as file:
        for idx_t in new_tasks:
            file.write("[ ] " + idx_t + "\n")


def remove_task(number):
    """Removes task from list of tasks with particular index.
    Argument - number.
    Raises Error -  if provided arguments aren't appropriate numbers.
    """
    list_to_del = set()
    tasks = read_file()
    try:
        for each_num in number:
            num_del = int(each_num) - 1
            if len(tasks) < (num_del + 1):
                print(f"Unable to remove: {each_num} index is out of bound")
            else:
                list_to_del.add(num_del)
        with open("todo.txt", "w", encoding="utf-8") as file:
            for num, line in enumerate(tasks):
                if num not in list_to_del:
                    file.write(line+"\n")
    except ValueError:
        print("Unable to remove: index is not a number")


def check_task(done):
    """To mark the task like done.
    Argument - number of line.
    Raises Error -  if provided arguments aren't appropriate numbers.
    """
    list_to_check = set()
    tasks = read_file()
    try:
        for each_task in done:
            num_check = int(each_task) - 1
            if len(tasks) < (num_check + 1):
                print(f"Unable to check: {each_task} index is out of bound")
            else:
                list_to_check.add(num_check)
        with open("todo.txt", "w", encoding="utf-8") as file:
            for num, line in enumerate(tasks):
                if num in list_to_check:
                    line = line.replace("[ ]", "[x]")
                file.write(line+"\n")
    except ValueError:
        print("Unable to check: index is not a number")


def info():
    """Prints usage functions of todo list."""
    text = (
        """Command Line Todo application
=============================

Command line arguments:
-l              Lists all the tasks
-a "todo task"  Adds a new task
-r _num_...     Removes an task
-c _num_...     Completes an task""")
    sys.stdout.buffer.write(text.encode("utf8"))


if __name__ == "__main__":
    args = sys.argv
    try:
        # print information
        if len(args) == 1:
            globals()["info"]()
    # wrong argument - print information
        elif args[1] in ["-a", "-r", "-c"]:
            # add tasks
            if args[1] == "-a":
                args[1] = "add_task"
                if len(args) < 3:
                    print("Unable to add: no task provided")
        # remove index task
            elif args[1] == "-r":
                args[1] = "remove_task"
                if len(args) < 3:
                    print("Unable to remove: no index provided")
        # done task
            elif args[1] == "-c":
                args[1] = "check_task"
                if len(args) < 3:
                    print("Unable to check: no index provided")
            globals()[args[1]](args[2:])
    # list tasks
        elif args[1] == "-l":
            args[1] = "list_items"
            globals()[args[1]]()
        else:
            print("Unsupported argument \n")
            globals()["info"]()

    except IndexError:
        print("Error")
