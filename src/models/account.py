from src.models import BaseModel
import datetime
import uuid

from peewee import *
from src.api import sys_log


class Account(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    email = CharField(max_length=255)
    mobile = CharField(max_length=255)
    firstname = CharField(max_length=255)
    middle_name = CharField(max_length=255)
    lastname = CharField(max_length=255)
    password_hash = CharField(max_length=255)
    avatar = CharField(max_length=255)
    last_login = DateTimeField(default=datetime.datetime.now)
    created_time = DateTimeField(default=datetime.datetime.now)
    updated_time = DateTimeField(default=datetime.datetime.now)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "mobile": self.mobile,
            "firstname": self.firstname,
            "middle_name": self.middle_name,
            "lastname": self.lastname,
            "password_hash": self.password_hash,
            "avatar": self.avatar,
            "last_login": self.last_login,
            "created_time": self.created_time,
            "updated_time": self.updated_time
        }

    def create_account(self):
        try:
            return Account.create(
                id=self.id,
                email=self.email,
                mobile=self.mobile,
                firstname=self.firstname,
                middle_name=self.middle_name,
                lastname=self.lastname,
                password_hash=self.password_hash,
                avatar=self.avatar,
                created_time=self.created_time,
                updated_time=self.updated_time
            )
        except Exception as ex:
            sys_log.logger.error("account::models::Account::create_account() error:%s" % str(ex))
            raise

    def check_account(self, email, password_hash):
        try:
            return Account.get(self.email == email, self.password_hash == password_hash)
        except Exception as ex:
            sys_log.logger.error("account::models::Account::check_account() error:%s" % str(ex))
            return None

