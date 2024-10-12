from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_type_holder_wrapped import MediaTypeHolderWrapped
from openapi_server import util


async def resources_media_types_format_get(request: web.Request, format) -> web.Response:
    """Get MediaTypes

    Information about media types

    :param format: Automatically added
    :type format: str

    """
    return web.Response(status=200)
