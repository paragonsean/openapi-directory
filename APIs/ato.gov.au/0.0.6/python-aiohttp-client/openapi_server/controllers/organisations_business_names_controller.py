from typing import List, Dict
from aiohttp import web

from openapi_server.models.business_name import BusinessName
from openapi_server.models.invalid_argument import InvalidArgument
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def organisations_party_id_business_names_get(request: web.Request, api_key, party_id) -> web.Response:
    """Retrieve a list of business names

    

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str

    """
    return web.Response(status=200)


async def organisations_party_id_business_names_post(request: web.Request, api_key, party_id, body) -> web.Response:
    """Create a business name

    Create a business name 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param body: Business Name resource
    :type body: dict | bytes

    """
    body = BusinessName.from_dict(body)
    return web.Response(status=200)


async def organisations_party_id_business_names_product_id_delete(request: web.Request, api_key, party_id, product_id) -> web.Response:
    """Delete a business name

    Delete a business name 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def organisations_party_id_business_names_product_id_get(request: web.Request, api_key, party_id, product_id) -> web.Response:
    """Retrieve a business name

    Retrieve a business name 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str

    """
    return web.Response(status=200)


async def organisations_party_id_business_names_product_id_put(request: web.Request, api_key, party_id, product_id, body) -> web.Response:
    """Update a business name

    Update a business name 

    :param api_key: The API key.
    :type api_key: str
    :param party_id: The party identifier.
    :type party_id: str
    :param product_id: The product identifier.
    :type product_id: str
    :param body: Business Name resource
    :type body: dict | bytes

    """
    body = BusinessName.from_dict(body)
    return web.Response(status=200)
