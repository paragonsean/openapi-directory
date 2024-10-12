from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation_layer_get400_response import AnnotationLayerGet400Response
from openapi_server import util


async def openapi_version_openapi_get(request: web.Request, version) -> web.Response:
    """openapi_version_openapi_get

    Get the OpenAPI spec for a specific API version

    :param version: 
    :type version: str

    """
    return web.Response(status=200)
