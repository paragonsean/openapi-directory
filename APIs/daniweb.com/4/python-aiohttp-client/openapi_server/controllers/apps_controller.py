from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_apps import EndpointGetApps
from openapi_server.models.endpoint_get_apps_id import EndpointGetAppsID
from openapi_server import util


async def apps_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """apps_get

    Fetch all Daniapps that are currently in production mode.

    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def apps_idget(request: web.Request, id) -> web.Response:
    """apps_idget

    Fetch an array of Daniapps that are currently in production mode.

    :param id: 
    :type id: List[int]

    """
    return web.Response(status=200)
