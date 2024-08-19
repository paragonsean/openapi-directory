from typing import List, Dict
from aiohttp import web

from openapi_server.models.name_type import NameType
from openapi_server.models.not_found import NotFound
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def classifications_name_types_get(request: web.Request, api_key) -> web.Response:
    """Retrieve a list of name types

    

    :param api_key: The API key.
    :type api_key: str

    """
    return web.Response(status=200)
