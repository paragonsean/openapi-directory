from typing import List, Dict
from aiohttp import web

from openapi_server.models.checkout_utility_request import CheckoutUtilityRequest
from openapi_server.models.checkout_utility_response import CheckoutUtilityResponse
from openapi_server import util


async def origin_keys_post(request: web.Request, body=None) -> web.Response:
    """Create originKey values for one or more merchant domains.

    This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.

    :param body: 
    :type body: dict | bytes

    """
    body = CheckoutUtilityRequest.from_dict(body)
    return web.Response(status=200)
