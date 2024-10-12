from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_order_management_v1_un_hold_post(request: web.Request, id) -> web.Response:
    """orders/{id}/unhold

    Releases a specified order from hold status.

    :param id: The order ID.
    :type id: int

    """
    return web.Response(status=200)
