from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.page import Page
from openapi_server.models.page_modify import PageModify
from openapi_server import util


async def pages_count_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Count all Pages.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def pages_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Page.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Page
    :type id: int

    """
    return web.Response(status=200)


async def pages_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Page by id.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Page
    :type id: int

    """
    return web.Response(status=200)


async def pages_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a Page.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Page
    :type id: int
    :param body: Page parameters.
    :type body: dict | bytes

    """
    body = PageModify.from_dict(body)
    return web.Response(status=200)


async def pages_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Pages.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def pages_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Page.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Page parameters.
    :type body: dict | bytes

    """
    body = PageModify.from_dict(body)
    return web.Response(status=200)
