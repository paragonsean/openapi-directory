from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_data_order_interface import SalesDataOrderInterface
from openapi_server.models.sales_order_repository_v1_save_post_request import SalesOrderRepositoryV1SavePostRequest
from openapi_server import util


async def sales_order_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """orders/

    Performs persist operations for a specified order.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesOrderRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
