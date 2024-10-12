from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.customer_group_repository_v1_save_post_request import CustomerGroupRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_group_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """customerGroups

    Save customer group.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerGroupRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
