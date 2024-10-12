from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_core_dto_accounting_plan import ApiCoreDtoAccountingPlan
from openapi_server.models.api_core_dto_accounting_user import ApiCoreDtoAccountingUser
from openapi_server import util


async def me_get_me(request: web.Request, ) -> web.Response:
    """Retrieve current account data

    


    """
    return web.Response(status=200)


async def me_get_me_plan(request: web.Request, ) -> web.Response:
    """Retrieve current account plan

    


    """
    return web.Response(status=200)
