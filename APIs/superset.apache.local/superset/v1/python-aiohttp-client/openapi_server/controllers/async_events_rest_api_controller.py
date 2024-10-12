from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server.models.async_event_get200_response import AsyncEventGet200Response
from openapi_server import util


async def async_event_get(request: web.Request, last_id=None) -> web.Response:
    """async_event_get

    Reads off of the Redis events stream, using the user&#39;s JWT token and optional query params for last event received.

    :param last_id: Last ID received by the client
    :type last_id: str

    """
    return web.Response(status=200)
