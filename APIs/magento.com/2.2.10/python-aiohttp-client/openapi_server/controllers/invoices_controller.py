from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_invoice_interface import SalesDataInvoiceInterface
from openapi_server.models.sales_invoice_repository_v1_save_post_request import SalesInvoiceRepositoryV1SavePostRequest
from openapi_server import util


async def sales_invoice_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """invoices/

    Performs persist operations for a specified invoice.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesInvoiceRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
