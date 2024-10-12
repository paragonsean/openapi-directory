from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_keys_dto import EndpointKeysDTO
from openapi_server.models.endpoint_settings_dto import EndpointSettingsDTO
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def endpoint_keys_get_keys(request: web.Request, ) -> web.Response:
    """Gets endpoint keys for an endpoint

    


    """
    return web.Response(status=200)


async def endpoint_settings_get_settings(request: web.Request, ) -> web.Response:
    """Gets endpoint settings for an endpoint.

    


    """
    return web.Response(status=200)
