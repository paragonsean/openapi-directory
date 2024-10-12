from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_address_request import AddAddressRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_addresses_response import GetAllAddressesResponse
from openapi_server import util


async def add_address(request: web.Request, body) -> web.Response:
    """Claim a new Mailscript address

    

    :param body: Address body
    :type body: dict | bytes

    """
    body = AddAddressRequest.from_dict(body)
    return web.Response(status=200)


async def delete_address(request: web.Request, address) -> web.Response:
    """Delete a mailscript address

    

    :param address: ID of address
    :type address: str

    """
    return web.Response(status=200)


async def get_all_addresses(request: web.Request, ) -> web.Response:
    """Get all addresses you have access to

    


    """
    return web.Response(status=200)
