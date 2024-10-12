from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_user_address_request import UpdateUserAddressRequest
from openapi_server.models.user_address200_response import UserAddress200Response
from openapi_server.models.user_address_request import UserAddressRequest
from openapi_server import util


async def update_user_address(request: web.Request, body) -> web.Response:
    """update the user&#39;s return address information

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = UpdateUserAddressRequest.from_dict(body)
    return web.Response(status=200)


async def user_address(request: web.Request, body=None) -> web.Response:
    """gets the user&#39;s return address information

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = UserAddressRequest.from_dict(body)
    return web.Response(status=200)
