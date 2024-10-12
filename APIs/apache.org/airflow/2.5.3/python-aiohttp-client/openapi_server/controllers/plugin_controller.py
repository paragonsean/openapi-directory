from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.plugin_collection import PluginCollection
from openapi_server import util


async def get_plugins(request: web.Request, limit=None, offset=None) -> web.Response:
    """Get a list of loaded plugins

    Get a list of loaded plugins.  *New in version 2.1.0* 

    :param limit: The numbers of items to return.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int

    """
    return web.Response(status=200)
