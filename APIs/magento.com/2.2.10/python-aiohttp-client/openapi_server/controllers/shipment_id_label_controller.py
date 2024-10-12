from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_shipment_management_v1_get_label_get(request: web.Request, id) -> web.Response:
    """shipment/{id}/label

    Gets a specified shipment label.

    :param id: The shipment label ID.
    :type id: int

    """
    return web.Response(status=200)
