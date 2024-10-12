from typing import List, Dict
from aiohttp import web

from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.license import License
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def individuals_party_id_licenses_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve a list of licenses

    

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_licenses_post(request: web.Request, api_key, party_id, body) -> web.Response:
    """Create a license

    Create a license 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: License resource
    :type body: dict | bytes

    """
    body = License.from_dict(body)
    return web.Response(status=200)


async def individuals_party_id_licenses_product_id_delete(request: web.Request, api_key, party_id, product_id) -> web.Response:
    """Delete a license

    Delete a license 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_licenses_product_id_get(request: web.Request, api_key, party_id, product_id) -> web.Response:
    """Retrieve a license

    Retrieve a license 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def individuals_party_id_licenses_product_id_put(request: web.Request, api_key, party_id, product_id, body) -> web.Response:
    """Update a license

    Update a license 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param body: License resource
    :type body: dict | bytes

    """
    body = License.from_dict(body)
    return web.Response(status=200)
