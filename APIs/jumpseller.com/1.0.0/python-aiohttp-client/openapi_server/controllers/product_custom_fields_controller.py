from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_product_custom_field import AddProductCustomField
from openapi_server.models.count import Count
from openapi_server.models.message_object import MessageObject
from openapi_server.models.not_found import NotFound
from openapi_server.models.product import Product
from openapi_server.models.product_custom_field import ProductCustomField
from openapi_server import util


async def products_id_fields_count_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Count all Product Custom Fields.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_fields_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Product Custom Fields

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_fields_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Add an existing Custom Field to a Product.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product Custom Field parameters.
    :type body: dict | bytes

    """
    body = AddProductCustomField.from_dict(body)
    return web.Response(status=200)


async def products_product_id_fields_field_id_json_delete(request: web.Request, login, authtoken, product_id, field_id) -> web.Response:
    """Delete value of Product Custom Field

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param product_id: Id of the Product.
    :type product_id: int
    :param field_id: Id of the Custom Field Value.
    :type field_id: int

    """
    return web.Response(status=200)


async def products_product_id_fields_field_id_json_put(request: web.Request, login, authtoken, product_id, field_id) -> web.Response:
    """Update value of Product Custom Field

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param product_id: Id of the Product.
    :type product_id: int
    :param field_id: Id of the Custom Field Value.
    :type field_id: int

    """
    return web.Response(status=200)
