from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_customer_group_config_v1_set_default_customer_group_put(request: web.Request, id) -> web.Response:
    """customerGroups/default/{id}

    Set system default customer group.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
