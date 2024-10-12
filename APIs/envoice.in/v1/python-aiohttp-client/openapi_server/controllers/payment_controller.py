from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_gateway_details_api_model import PaymentGatewayDetailsApiModel
from openapi_server import util


async def payment_api_supported(request: web.Request, x_auth_key, x_auth_secret) -> web.Response:
    """Return all supported payment gateways (no currencies means all are supported)

    

    :param x_auth_key: 
    :type x_auth_key: str
    :param x_auth_secret: 
    :type x_auth_secret: str

    """
    return web.Response(status=200)
