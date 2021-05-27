from functools import wraps

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.common.exception import InputParamError, CustomError
from src.common.logging import SystemLog

app = FastAPI()

sys_log = SystemLog()


def build_message_response(message=None, code=None, data=None, paging=None):
    code = 200 if not code else code
    result = {"message": message, "code": code}
    if data:
        result["data"] = data
    if paging:
        result["paging"] = paging

    return result


def try_except_response(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            sys_log.logger.debug("message: {}".format(str(func(*args, **kwargs))))
            return JSONResponse(status_code=200, content=func(*args, **kwargs))
        except InputParamError as InPE:
            sys_log.logger.debug("message: {}".format(InPE.message))
            return JSONResponse(status_code=412, content=build_message_response(InPE.message, 412))
        except CustomError as CuE:
            sys_log.logger.debug("message: {}".format(CuE.message))
            return JSONResponse(status_code=413, content=build_message_response(CuE.message, 413))
        except Exception as e:
            sys_log.logger.error("Error: {}".format(e))
            return JSONResponse(status_code=500, content=build_message_response(
                message="Error server!",
                code=500
            ))

    return wrapper
