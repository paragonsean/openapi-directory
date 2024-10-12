from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_address import DeleteAddress
from openapi_server.models.delete_address_request import DeleteAddressRequest
from openapi_server.models.export_address import ExportAddress
from openapi_server.models.export_address_request import ExportAddressRequest
from openapi_server.models.import_address import ImportAddress
from openapi_server.models.import_address_request import ImportAddressRequest
from openapi_server.models.list_addresses import ListAddresses
from openapi_server.models.new_address import NewAddress
from openapi_server.models.new_address_request import NewAddressRequest
from openapi_server import util


async def delete_address(request: web.Request, authorization, body) -> web.Response:
    """deleteAddress

    Deletes an existing ethereum address. Be careful when using this function.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAddressRequest.from_dict(body)
    return web.Response(status=200)


async def export_address(request: web.Request, authorization, body) -> web.Response:
    """exportAddress

    Returns all ethereum addresses created with an account.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExportAddressRequest.from_dict(body)
    return web.Response(status=200)


async def import_address(request: web.Request, authorization, body) -> web.Response:
    """importAddress

    Returns all ethereum addresses created with an account.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ImportAddressRequest.from_dict(body)
    return web.Response(status=200)


async def list_addresses(request: web.Request, content_type, authorization) -> web.Response:
    """listAddresses

    Returns all ethereum addresses created with an account.

    :param content_type: 
    :type content_type: str
    :param authorization: API Key
    :type authorization: str

    """
    return web.Response(status=200)


async def new_address(request: web.Request, authorization, body) -> web.Response:
    """newAddress

    Generates a new ethereum addresses you can use to send or receive funds. Do not lose the password! We can&#39;t restore access to an address if you lose it.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = NewAddressRequest.from_dict(body)
    return web.Response(status=200)
