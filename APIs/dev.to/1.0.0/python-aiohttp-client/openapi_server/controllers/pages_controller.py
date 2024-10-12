from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_pages_post_request import ApiPagesPostRequest
from openapi_server.models.page import Page
from openapi_server import util


async def api_pages_get(request: web.Request, ) -> web.Response:
    """show details for all pages

    This endpoint allows the client to retrieve details for all Page objects.


    """
    return web.Response(status=200)


async def api_pages_id_delete(request: web.Request, id) -> web.Response:
    """remove a page

    This endpoint allows the client to delete a single Page object, specified by ID.

    :param id: The ID of the page.
    :type id: int

    """
    return web.Response(status=200)


async def api_pages_id_get(request: web.Request, id) -> web.Response:
    """show details for a page

    This endpoint allows the client to retrieve details for a single Page object, specified by ID.

    :param id: The ID of the page.
    :type id: int

    """
    return web.Response(status=200)


async def api_pages_id_put(request: web.Request, id, body=None) -> web.Response:
    """update details for a page

    This endpoint allows the client to retrieve details for a single Page object, specified by ID.

    :param id: The ID of the page.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Page.from_dict(body)
    return web.Response(status=200)


async def api_pages_post(request: web.Request, body=None) -> web.Response:
    """pages

    This endpoint allows the client to create a new page.

    :param body: 
    :type body: dict | bytes

    """
    body = ApiPagesPostRequest.from_dict(body)
    return web.Response(status=200)
