from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server import util


async def resolve_image_using_get(request: web.Request, image_id) -> web.Response:
    """Resolve image

    

    :param image_id: The id of the image to be resolved.
    :type image_id: str

    """
    return web.Response(status=200)
