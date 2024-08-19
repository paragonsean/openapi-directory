from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.payment_method import PaymentMethod
from openapi_server import util


async def payment_methods_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Payment Method.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Payment Method
    :type id: int

    """
    return web.Response(status=200)


async def payment_methods_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all Store&#39;s Payment Methods.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)
