from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_overview import ApiOverview
from openapi_server.models.meta_root200_response import MetaRoot200Response
from openapi_server import util


async def meta_get(request: web.Request, ) -> web.Response:
    """Get GitHub Enterprise Server meta information

    


    """
    return web.Response(status=200)


async def meta_get_octocat(request: web.Request, s=None) -> web.Response:
    """Get Octocat

    Get the octocat as ASCII art

    :param s: The words to show in Octocat&#39;s speech bubble
    :type s: str

    """
    return web.Response(status=200)


async def meta_get_zen(request: web.Request, ) -> web.Response:
    """Get the Zen of GitHub

    Get a random sentence from the Zen of GitHub


    """
    return web.Response(status=200)


async def meta_root(request: web.Request, ) -> web.Response:
    """GitHub API Root

    Get Hypermedia links to resources accessible in GitHub&#39;s REST API


    """
    return web.Response(status=200)
