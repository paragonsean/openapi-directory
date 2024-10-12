from typing import List, Dict
from aiohttp import web

from openapi_server.models.landlord_photo_model_results import LandlordPhotoModelResults
from openapi_server import util


async def property_controller_get_properties_photos(request: web.Request, short_name, token, property_id, offset, count) -> web.Response:
    """A collection showing all the photos linked to a specific block, property or room

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param token: The login token returned from the /session POST call
    :type token: str
    :param property_id: The unique ID of the Property
    :type property_id: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)
