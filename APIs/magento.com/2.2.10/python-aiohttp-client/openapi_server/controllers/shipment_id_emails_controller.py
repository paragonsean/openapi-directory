from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_shipment_management_v1_notify_post(request: web.Request, id) -> web.Response:
    """shipment/{id}/emails

    Emails user a specified shipment.

    :param id: The shipment ID.
    :type id: int

    """
    return web.Response(status=200)
