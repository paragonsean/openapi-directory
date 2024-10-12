from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_jo import ErrorJO
from openapi_server.models.rental_object_jo import RentalObjectJO
from openapi_server import util


async def list_booking_proposals(request: web.Request, lat=None, lon=None, radius=None, offset=None, limit=None, providernetwork=None, begin=None, end=None, expand=None, view=None) -> web.Response:
    """Query for available RentalObjects of a specific view

    Here you can query all bookable Rental Objects with different Parameters (Time, Location,...)

    :param lat: 
    :type lat: float
    :param lon: 
    :type lon: float
    :param radius: 
    :type radius: int
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param providernetwork: 
    :type providernetwork: str
    :param begin: 
    :type begin: str
    :param end: 
    :type end: str
    :param expand: 
    :type expand: str
    :param view: 
    :type view: str

    """
    return web.Response(status=200)
