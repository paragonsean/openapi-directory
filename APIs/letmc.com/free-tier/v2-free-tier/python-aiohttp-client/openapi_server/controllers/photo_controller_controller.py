from typing import List, Dict
from aiohttp import web

from openapi_server.models.photo_model import PhotoModel
from openapi_server.models.photo_model_results import PhotoModelResults
from openapi_server import util


async def photo_controller_get_photo_download(request: web.Request, short_name, photo_id, width=None, height=None) -> web.Response:
    """Downloads the photo of a property given the property and photo ID.

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param photo_id: The unique ID of the photo on the property
    :type photo_id: str
    :param width: An optional parameter specifying the image width
    :type width: int
    :param height: An optional parameter specifying the image height
    :type height: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_photo_photos_get(request: web.Request, short_name, offset, count) -> web.Response:
    """A collection of all photos in the company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)


async def v2_tier1_short_name_photo_photos_photo_idget(request: web.Request, short_name, photo_id) -> web.Response:
    """Get a specific photo given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param photo_id: The unique ID of the Photo
    :type photo_id: str

    """
    return web.Response(status=200)
