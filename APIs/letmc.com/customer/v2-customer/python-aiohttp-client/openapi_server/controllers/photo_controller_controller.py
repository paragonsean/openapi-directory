from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def photo_controller_get_photo_download(request: web.Request, short_name, token, photo_id, width=None, height=None) -> web.Response:
    """Downloads the photo of a property given the photo ID.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param photo_id: The unique ID of the photo on the property
    :type photo_id: str
    :param width: An optional parameter specifying the image width
    :type width: int
    :param height: An optional parameter specifying the image height
    :type height: int

    """
    return web.Response(status=200)
