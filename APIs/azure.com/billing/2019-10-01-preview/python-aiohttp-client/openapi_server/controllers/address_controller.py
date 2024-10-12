from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_details import AddressDetails
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.validate_address_response import ValidateAddressResponse
from openapi_server import util


async def address_validate(request: web.Request, api_version, address) -> web.Response:
    """address_validate

    Validates the address.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param address: 
    :type address: dict | bytes

    """
    address = AddressDetails.from_dict(address)
    return web.Response(status=200)
