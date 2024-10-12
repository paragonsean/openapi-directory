from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_invoice_interface import SalesDataInvoiceInterface
from openapi_server import util


async def sales_invoice_repository_v1_get_get(request: web.Request, id) -> web.Response:
    """invoices/{id}

    Loads a specified invoice.

    :param id: The invoice ID.
    :type id: int

    """
    return web.Response(status=200)
