from src.controllers import BaseController
from src.api import build_message_response
from src.common.exception import InputParamError, CustomError
from src.models.account import Account as AccountModel
from src.common.utils import generate_md5_by_str


class Account(BaseController):

    def login(self, body):
        password_hash = generate_md5_by_str(body.password)
        email = body.email

        check_account = AccountModel().check_account(
            email=email,
            password_hash=password_hash
        )
        if check_account:
            return build_message_response(message="Login successes!!")
        return build_message_response(message="abc")

    def register(self, body_register):
        pass
