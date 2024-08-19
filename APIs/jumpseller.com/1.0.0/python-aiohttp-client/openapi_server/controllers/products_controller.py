from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.product import Product
from openapi_server.models.product_edit import ProductEdit
from openapi_server.models.status_invalid import StatusInvalid
from openapi_server import util


async def products_after_id_json_get(request: web.Request, login, authtoken, id, locale=None) -> web.Response:
    """Retrieves Products after the given id.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_category_category_id_count_json_get(request: web.Request, login, authtoken, category_id, locale=None) -> web.Response:
    """Count Products filtered by category.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param category_id: Category ID of the Product used as filter
    :type category_id: int
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_category_category_id_json_get(request: web.Request, login, authtoken, category_id, locale=None) -> web.Response:
    """Retrieve Products filtered by category.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param category_id: Category ID of the Product used as filter
    :type category_id: int
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Products.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def products_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Product.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_json_get(request: web.Request, login, authtoken, id, locale=None) -> web.Response:
    """Retrieve a single Product.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_id_json_put(request: web.Request, login, authtoken, id, body, locale=None) -> web.Response:
    """Modify an existing Product.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product parameters to change
    :type body: dict | bytes
    :param locale: Locale code of the translation
    :type locale: str

    """
    body = ProductEdit.from_dict(body)
    return web.Response(status=200)


async def products_json_get(request: web.Request, login, authtoken, limit=None, page=None, locale=None) -> web.Response:
    """Retrieve all Products.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_json_post(request: web.Request, login, authtoken, body, locale=None) -> web.Response:
    """Create a new Product.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Product parameters.
    :type body: dict | bytes
    :param locale: Locale code of the translation
    :type locale: str

    """
    body = ProductEdit.from_dict(body)
    return web.Response(status=200)


async def products_search_json_get(request: web.Request, login, authtoken, query, locale=None, fields=None) -> web.Response:
    """Retrieve a Product List from a query.

    Endpoint example:   &#x60;&#x60;&#x60;text https://api.jumpseller.com/v1/products/search.json?login&#x3D;XXXXXX&amp;authtoken&#x3D;XXXXX&amp;query&#x3D;test&amp;fields&#x3D;name,description  &#x60;&#x60;&#x60;

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param query: Text to query for the Product
    :type query: str
    :param locale: Locale code of the translation
    :type locale: str
    :param fields: Comma separated values of the fields to query for the Product
    :type fields: str

    """
    return web.Response(status=200)


async def products_status_status_count_json_get(request: web.Request, login, authtoken, status, locale=None) -> web.Response:
    """Count Products filtered by status.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param status: Status of the Product used as filter
    :type status: str
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)


async def products_status_status_json_get(request: web.Request, login, authtoken, status, locale=None) -> web.Response:
    """Retrieve Products filtered by status.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param status: Status of the Product used as filter
    :type status: str
    :param locale: Locale code of the translation
    :type locale: str

    """
    return web.Response(status=200)
