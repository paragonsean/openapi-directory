from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_creditmemo_repository_v1_save_post_request import SalesCreditmemoRepositoryV1SavePostRequest
from openapi_server.models.sales_data_creditmemo_interface import SalesDataCreditmemoInterface
from openapi_server import util


async def sales_creditmemo_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """creditmemo

    Performs persist operations for a specified credit memo.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesCreditmemoRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
