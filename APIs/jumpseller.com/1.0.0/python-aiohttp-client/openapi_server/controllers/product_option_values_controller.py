from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.product_option_value import ProductOptionValue
from openapi_server.models.product_option_value_edit import ProductOptionValueEdit
from openapi_server import util


async def products_id_options_option_id_values_count_json_get(request: web.Request, login, authtoken, id, option_id) -> web.Response:
    """Count all Product Option Values.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int
    :param option_id: ID of the Product Option
    :type option_id: int

    """
    return web.Response(status=200)


async def products_id_options_option_id_values_json_get(request: web.Request, login, authtoken, id, option_id) -> web.Response:
    """Retrieve all Product Option Values.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int
    :param option_id: ID of the Product Option
    :type option_id: int

    """
    return web.Response(status=200)


async def products_id_options_option_id_values_json_post(request: web.Request, login, authtoken, id, option_id, body) -> web.Response:
    """Create a new Product Option Value.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param option_id: Id of the Product Option
    :type option_id: int
    :param body: Product Option Value parameters.
    :type body: dict | bytes

    """
    body = ProductOptionValueEdit.from_dict(body)
    return web.Response(status=200)


async def products_id_options_option_id_values_value_id_json_delete(request: web.Request, login, authtoken, id, option_id, value_id) -> web.Response:
    """Delete a Product Option Value.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param option_id: Id of the Product Option
    :type option_id: int
    :param value_id: ID of the Product Option Value
    :type value_id: int

    """
    return web.Response(status=200)


async def products_id_options_option_id_values_value_id_json_get(request: web.Request, login, authtoken, id, option_id, value_id) -> web.Response:
    """Retrieve a single Product Option Value.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param option_id: Id of the Product Option
    :type option_id: int
    :param value_id: ID of the Product Option Value
    :type value_id: int

    """
    return web.Response(status=200)


async def products_id_options_option_id_values_value_id_json_put(request: web.Request, login, authtoken, id, option_id, value_id, body) -> web.Response:
    """Modify an existing Product Option Value.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param option_id: Id of the Product Option
    :type option_id: int
    :param value_id: Id of the Product Option Value
    :type value_id: int
    :param body: Product option value parameters to change
    :type body: dict | bytes

    """
    body = ProductOptionValueEdit.from_dict(body)
    return web.Response(status=200)
