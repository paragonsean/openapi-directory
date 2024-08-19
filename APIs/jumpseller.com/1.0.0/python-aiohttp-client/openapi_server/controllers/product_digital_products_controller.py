from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.digital_product import DigitalProduct
from openapi_server.models.digital_product_edit import DigitalProductEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def products_id_digital_products_count_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Count all Product DigitalProducts.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_digital_products_digital_product_id_json_delete(request: web.Request, login, authtoken, id, digital_product_id) -> web.Response:
    """Delete a Product DigitalProduct.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param digital_product_id: Id of the Product DigitalProduct
    :type digital_product_id: int

    """
    return web.Response(status=200)


async def products_id_digital_products_digital_product_id_json_get(request: web.Request, login, authtoken, id, digital_product_id) -> web.Response:
    """Retrieve a single Product DigitalProduct.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param digital_product_id: Id of the Product DigitalProduct
    :type digital_product_id: int

    """
    return web.Response(status=200)


async def products_id_digital_products_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Product DigitalProducts.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_digital_products_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Product DigitalProduct.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product DigitalProduct parameters.
    :type body: dict | bytes

    """
    body = DigitalProductEdit.from_dict(body)
    return web.Response(status=200)
