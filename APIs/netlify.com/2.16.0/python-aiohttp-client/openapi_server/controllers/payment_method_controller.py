from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.payment_method import PaymentMethod
from openapi_server import util


async def list_payment_methods_for_user(request: web.Request, ) -> web.Response:
    """list_payment_methods_for_user

    


    """
    return web.Response(status=200)
