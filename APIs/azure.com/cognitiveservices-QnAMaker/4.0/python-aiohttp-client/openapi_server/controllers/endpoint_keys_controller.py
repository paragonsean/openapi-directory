from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_keys_dto import EndpointKeysDTO
from openapi_server.models.endpoint_settings_dto import EndpointSettingsDTO
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def endpoint_keys_refresh_keys(request: web.Request, key_type) -> web.Response:
    """Re-generates an endpoint key.

    

    :param key_type: Type of Key
    :type key_type: str

    """
    return web.Response(status=200)


async def endpoint_settings_update_settings(request: web.Request, endpoint_settings_payload) -> web.Response:
    """Updates endpoint settings for an endpoint.

    

    :param endpoint_settings_payload: Post body of the request.
    :type endpoint_settings_payload: dict | bytes

    """
    endpoint_settings_payload = EndpointSettingsDTO.from_dict(endpoint_settings_payload)
    return web.Response(status=200)
