from peewee import *
from playhouse.db_url import connect

from config import MySQL
from src.api import sys_log


def init_database():
    sys_log.logger.info("models::__init__()::init_database: url = %s" % MySQL.TODOLIST_URI)
    return connect(MySQL.TODOLIST_URI)


database = init_database()


class BaseModel(Model):
    class Meta:
        database = database
