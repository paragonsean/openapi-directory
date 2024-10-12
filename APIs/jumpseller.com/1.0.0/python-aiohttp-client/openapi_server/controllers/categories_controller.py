from typing import List, Dict
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.category_edit import CategoryEdit
from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def categories_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Categories.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def categories_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Category.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Category
    :type id: int

    """
    return web.Response(status=200)


async def categories_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Category.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Category
    :type id: int

    """
    return web.Response(status=200)


async def categories_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Modify an existing Category.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Category
    :type id: int
    :param body: Category parameters.
    :type body: dict | bytes

    """
    body = CategoryEdit.from_dict(body)
    return web.Response(status=200)


async def categories_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all Categories.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def categories_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Category.

    Category&#39;s permalink is automatically generated from the given category&#39;s name.

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Category parameters.
    :type body: dict | bytes

    """
    body = CategoryEdit.from_dict(body)
    return web.Response(status=200)
