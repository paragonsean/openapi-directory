from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_item_interface import SalesDataOrderItemInterface
from openapi_server import util


async def sales_order_item_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """orders/items/{id}

    Loads a specified order item.

    :param id: The order item ID.
    :type id: int

    """
    return web.Response(status=200)
