from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_group_interface import CustomerDataGroupInterface
from openapi_server.models.customer_group_repository_v1_save_post_request import CustomerGroupRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_group_repository_v1_delete_by_id_delete(request: web.Request, id) -> web.Response:
    """customerGroups/{id}

    Delete customer group by ID.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def customer_group_repository_v1_get_by_id_get(request: web.Request, id) -> web.Response:
    """customerGroups/{id}

    Get customer group by group ID.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def customer_group_repository_v1_save_put(request: web.Request, id, body=None) -> web.Response:
    """customerGroups/{id}

    Save customer group.

    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CustomerGroupRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
