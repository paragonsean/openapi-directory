from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_balance_balance_management_from_quote_v1_apply_post(request: web.Request, ) -> web.Response:
    """carts/mine/balance/apply

    Apply store credit.


    """
    return web.Response(status=200)
