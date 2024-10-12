from typing import List, Dict
from aiohttp import web

from openapi_server.models.requests import Requests
from openapi_server import util


async def api_baskets_name_requests_delete(request: web.Request, name) -> web.Response:
    """Delete all requests

    Deletes all requests collected by this basket.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def api_baskets_name_requests_get(request: web.Request, name, max=None, skip=None, q=None, _in=None) -> web.Response:
    """Get collected requests

    Fetches collection of requests collected by this basket.

    :param name: The basket name
    :type name: str
    :param max: Maximum number of requests to return; default 20
    :type max: int
    :param skip: Number of requests to skip; default 0
    :type skip: int
    :param q: Query string to filter result, only requests that match the query will be included in response
    :type q: str
    :param _in: Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60; 
    :type _in: str

    """
    return web.Response(status=200)


async def baskets_name_requests_delete(request: web.Request, name) -> web.Response:
    """Delete all requests

    Deletes all requests collected by this basket.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def baskets_name_requests_get(request: web.Request, name, max=None, skip=None, q=None, _in=None) -> web.Response:
    """Get collected requests

    Fetches collection of requests collected by this basket.

    :param name: The basket name
    :type name: str
    :param max: Maximum number of requests to return; default 20
    :type max: int
    :param skip: Number of requests to skip; default 0
    :type skip: int
    :param q: Query string to filter result, only requests that match the query will be included in response
    :type q: str
    :param _in: Defines what is taken into account when filtering is applied: &#x60;body&#x60; - search in content body of collected requests, &#x60;query&#x60; - search among query parameters of collected requests, &#x60;headers&#x60; - search among request header values, &#x60;any&#x60; - search anywhere; default &#x60;any&#x60; 
    :type _in: str

    """
    return web.Response(status=200)
