import os
from config import TodoList

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"

LOG_DIR = os.path.join(TodoList.TODOLIST_HOME, TodoList.FOLDER_LOG)
FILE_LOG = os.path.join(LOG_DIR, "app.log")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_CONF_FILE = os.path.join(TodoList.TODOLIST_HOME, "resources", "configs", "log.conf")
