from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.registered_identifier_type import RegisteredIdentifierType
from openapi_server.models.unauthenticated import Unauthenticated
from openapi_server import util


async def classifications_registered_identifier_types_get(request: web.Request, api_key) -> web.Response:
    """Retrieve a list of registered identifier types

    

    :param api_key: The API key.
    :type api_key: str

    """
    return web.Response(status=200)
