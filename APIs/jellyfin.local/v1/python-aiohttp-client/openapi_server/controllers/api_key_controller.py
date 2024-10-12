from typing import List, Dict
from aiohttp import web

from openapi_server.models.authentication_info_query_result import AuthenticationInfoQueryResult
from openapi_server import util


async def create_key(request: web.Request, app) -> web.Response:
    """Create a new api key.

    

    :param app: Name of the app using the authentication key.
    :type app: str

    """
    return web.Response(status=200)


async def get_keys(request: web.Request, ) -> web.Response:
    """Get all keys.

    


    """
    return web.Response(status=200)


async def revoke_key(request: web.Request, key) -> web.Response:
    """Remove an api key.

    

    :param key: The access token to delete.
    :type key: str

    """
    return web.Response(status=200)
