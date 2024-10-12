from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_address_repository_v1_delete_by_id_delete(request: web.Request, address_id) -> web.Response:
    """addresses/{addressId}

    Delete customer address by ID.

    :param address_id: 
    :type address_id: int

    """
    return web.Response(status=200)
