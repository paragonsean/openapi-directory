from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_attribute_group_repository_v1_delete_by_id_delete(request: web.Request, group_id) -> web.Response:
    """products/attribute-sets/groups/{groupId}

    Remove attribute group by id

    :param group_id: 
    :type group_id: int

    """
    return web.Response(status=200)
