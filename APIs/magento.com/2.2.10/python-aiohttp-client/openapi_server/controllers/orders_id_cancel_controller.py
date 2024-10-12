from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_order_management_v1_cancel_post(request: web.Request, id) -> web.Response:
    """orders/{id}/cancel

    Cancels a specified order.

    :param id: The order ID.
    :type id: int

    """
    return web.Response(status=200)
