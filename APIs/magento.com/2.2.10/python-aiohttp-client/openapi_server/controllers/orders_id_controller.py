from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_interface import SalesDataOrderInterface
from openapi_server import util


async def sales_order_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """orders/{id}

    Loads a specified order.

    :param id: The order ID.
    :type id: int

    """
    return web.Response(status=200)
