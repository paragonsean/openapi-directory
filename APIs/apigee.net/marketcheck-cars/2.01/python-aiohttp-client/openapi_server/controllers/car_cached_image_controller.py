from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def get_cached_image(request: web.Request, listing_id, image_id, api_key=None) -> web.Response:
    """Fetch cached image

    Fetch the cached car image

    :param listing_id: ID of the listing to fetch cached images for
    :type listing_id: str
    :param image_id: ID of the image to fetch
    :type image_id: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)
