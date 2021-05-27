from src.api import app
from src.api.v1_0.check_services import check_services_router
from src.api.v1_0.account import account_router

api_prefix = "/api/v1.0"

app.include_router(router=check_services_router, prefix=api_prefix)
app.include_router(router=account_router, prefix=api_prefix)

