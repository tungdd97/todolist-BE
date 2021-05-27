import os


class MySQL:
    TODOLIST_URI = os.environ.get("TODOLIST_URI")


class TodoList:
    TODOLIST_HOME = os.environ.get("TODOLIST_HOME")
    FOLDER_LOG = os.environ.get("FOLDER_LOG")
