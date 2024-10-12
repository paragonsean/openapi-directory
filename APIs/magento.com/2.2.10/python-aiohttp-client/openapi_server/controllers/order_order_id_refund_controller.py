from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_refund_order_v1_execute_post_request import SalesRefundOrderV1ExecutePostRequest
from openapi_server import util


async def sales_refund_order_v1_execute_post(request: web.Request, order_id, body=None) -> web.Response:
    """order/{orderId}/refund

    Create offline refund for order

    :param order_id: 
    :type order_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SalesRefundOrderV1ExecutePostRequest.from_dict(body)
    return web.Response(status=200)
