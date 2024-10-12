from typing import List, Dict
from aiohttp import web

from openapi_server.models.room_type import RoomType
from openapi_server import util


async def room_types_get_room_type(request: web.Request, app_id, app_key, hotel_id, code) -> web.Response:
    """Get all the details for a specific room type in the hotel.

    With this call you can load the details about a specific room type in the hotel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the room type belongs to.
    :type hotel_id: int
    :param code: The code of the room type you want to see details for.
    :type code: str

    """
    return web.Response(status=200)


async def room_types_get_room_types(request: web.Request, app_id, app_key, hotel_id) -> web.Response:
    """Get a list with the details of all room types for for the specified hotel id.

    With this call you can load the details about a all available room types for the specified hotel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: The hotel id the room type belongs to.
    :type hotel_id: int

    """
    return web.Response(status=200)
