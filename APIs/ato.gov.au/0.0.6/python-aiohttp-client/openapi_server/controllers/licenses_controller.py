from typing import List, Dict
from aiohttp import web

from openapi_server.models.license import License
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def licenses_get(request: web.Request, api_key) -> web.Response:
    """Retrieve a list of licenses

    Retrieve a list of licenses 

    :param api_key: The API key.
    :type api_key: str

    """
    return web.Response(status=200)
