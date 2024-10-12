from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_invoice_order_v1_execute_post_request import SalesInvoiceOrderV1ExecutePostRequest
from openapi_server import util


async def sales_invoice_order_v1_execute_post(request: web.Request, order_id, body=None) -> web.Response:
    """order/{orderId}/invoice

    

    :param order_id: 
    :type order_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SalesInvoiceOrderV1ExecutePostRequest.from_dict(body)
    return web.Response(status=200)
