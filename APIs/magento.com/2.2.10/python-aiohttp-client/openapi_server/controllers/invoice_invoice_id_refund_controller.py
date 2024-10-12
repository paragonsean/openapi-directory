from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_refund_invoice_v1_execute_post_request import SalesRefundInvoiceV1ExecutePostRequest
from openapi_server import util


async def sales_refund_invoice_v1_execute_post(request: web.Request, invoice_id, body=None) -> web.Response:
    """invoice/{invoiceId}/refund

    Create refund for invoice

    :param invoice_id: 
    :type invoice_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SalesRefundInvoiceV1ExecutePostRequest.from_dict(body)
    return web.Response(status=200)
