from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_creditmemo_management_v1_refund_post_request import SalesCreditmemoManagementV1RefundPostRequest
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface
from openapi_server import util


async def sales_creditmemo_management_v1_refund_post(request: web.Request, body=None) -> web.Response:
    """creditmemo/refund

    Prepare creditmemo to refund and save it.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesCreditmemoManagementV1RefundPostRequest.from_dict(body)
    return web.Response(status=200)
