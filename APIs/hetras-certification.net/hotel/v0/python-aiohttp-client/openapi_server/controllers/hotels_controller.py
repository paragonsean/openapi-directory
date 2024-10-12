from typing import List, Dict
from aiohttp import web

from openapi_server.models.hotel import Hotel
from openapi_server import util


async def hotels_get_hotel(request: web.Request, app_id, app_key, hotel_id) -> web.Response:
    """Get the details of the hotel with the speccified hotel id.

    Load the details about the specified hotel.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str
    :param hotel_id: 
    :type hotel_id: int

    """
    return web.Response(status=200)


async def hotels_get_hotels(request: web.Request, app_id, app_key) -> web.Response:
    """Get a list of all the hotels of a chain your application has access to.

    Load the details about all the hotels your application has access to.

    :param app_id: Application identifier
    :type app_id: str
    :param app_key: Application key.
    :type app_key: str

    """
    return web.Response(status=200)
