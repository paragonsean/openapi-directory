from typing import List, Dict
from aiohttp import web

from openapi_server.models.credits_response import CreditsResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def credits_balance_get(request: web.Request, ) -> web.Response:
    """credits_balance_get

    Returns the number of credits currently available on the account


    """
    return web.Response(status=200)
