from typing import List, Dict
from aiohttp import web

from openapi_server.models.electronic_address import ElectronicAddress
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def individuals_party_id_electronic_addresses_address_id_delete(request: web.Request, api_key, party_id, address_id) -> web.Response:
    """Delete an electronic address

    Delete an electronic address 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param address_id: The address identifier.
    :type address_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_electronic_addresses_address_id_get(request: web.Request, api_key, party_id, address_id) -> web.Response:
    """Retrieve an electronic address

    Retrieve an electronic address 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param address_id: The address identifier.
    :type address_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_electronic_addresses_address_id_put(request: web.Request, api_key, party_id, address_id, body) -> web.Response:
    """Update an electronic address

    Update an electronic address 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param address_id: The address identifier.
    :type address_id: str
    :param body: Electronic Address resource
    :type body: dict | bytes

    """
    body = ElectronicAddress.from_dict(body)
    return web.Response(status=200)


async def individuals_party_id_electronic_addresses_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve a list of electronic addresses

    

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_electronic_addresses_post(request: web.Request, api_key, party_id, body) -> web.Response:
    """Create an electronic address

    Create an electronic address 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: Electronic Address resource
    :type body: dict | bytes

    """
    body = ElectronicAddress.from_dict(body)
    return web.Response(status=200)
