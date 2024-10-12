from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_data_address_interface import CustomerDataAddressInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def customer_address_repository_v1_get_by_id_get(request: web.Request, address_id) -> web.Response:
    """customers/addresses/{addressId}

    Retrieve customer address.

    :param address_id: 
    :type address_id: int

    """
    return web.Response(status=200)
