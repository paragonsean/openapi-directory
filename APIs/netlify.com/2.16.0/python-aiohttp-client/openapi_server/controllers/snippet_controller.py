from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.snippet import Snippet
from openapi_server import util


async def create_site_snippet(request: web.Request, site_id, snippet) -> web.Response:
    """create_site_snippet

    

    :param site_id: 
    :type site_id: str
    :param snippet: 
    :type snippet: dict | bytes

    """
    snippet = Snippet.from_dict(snippet)
    return web.Response(status=200)


async def delete_site_snippet(request: web.Request, site_id, snippet_id) -> web.Response:
    """delete_site_snippet

    

    :param site_id: 
    :type site_id: str
    :param snippet_id: 
    :type snippet_id: str

    """
    return web.Response(status=200)


async def get_site_snippet(request: web.Request, site_id, snippet_id) -> web.Response:
    """get_site_snippet

    

    :param site_id: 
    :type site_id: str
    :param snippet_id: 
    :type snippet_id: str

    """
    return web.Response(status=200)


async def list_site_snippets(request: web.Request, site_id) -> web.Response:
    """list_site_snippets

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_site_snippet(request: web.Request, site_id, snippet_id, snippet) -> web.Response:
    """update_site_snippet

    

    :param site_id: 
    :type site_id: str
    :param snippet_id: 
    :type snippet_id: str
    :param snippet: 
    :type snippet: dict | bytes

    """
    snippet = Snippet.from_dict(snippet)
    return web.Response(status=200)
