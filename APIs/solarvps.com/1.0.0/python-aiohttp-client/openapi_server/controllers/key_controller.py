from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def key_generate_get(request: web.Request, username, password) -> web.Response:
    """Generate API Key

    API Key is regenerated if it already exists

    :param username: Email address used to login to SolarSystem
    :type username: str
    :param password: Password used to login to SolarSystem
    :type password: str

    """
    return web.Response(status=200)


async def key_get_get(request: web.Request, username, password) -> web.Response:
    """Get API Key

    Gets the API Key for user

    :param username: Email address used to login to SolarSystem
    :type username: str
    :param password: Password used to login to SolarSystem
    :type password: str

    """
    return web.Response(status=200)
