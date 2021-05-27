from fastapi import APIRouter

from src.api import try_except_response, build_message_response
from src.api.uri import URI
from src.schemas.v1_0.account import Login, Register
from src.controllers.account import Account

account_router = APIRouter()


@account_router.post(URI.LOGIN)
@try_except_response
def login(body_login: Login):
    return Account().login(body_login)


@account_router.post(URI.REGISTER)
@try_except_response
def register(body_register: Register):
    return Account().register(body_register)
