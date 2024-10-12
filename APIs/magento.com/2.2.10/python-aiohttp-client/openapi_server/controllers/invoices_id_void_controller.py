from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_invoice_management_v1_set_void_post(request: web.Request, id) -> web.Response:
    """invoices/{id}/void

    Voids a specified invoice.

    :param id: The invoice ID.
    :type id: int

    """
    return web.Response(status=200)
