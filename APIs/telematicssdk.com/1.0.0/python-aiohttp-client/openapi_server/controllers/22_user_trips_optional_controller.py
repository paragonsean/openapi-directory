from typing import List, Dict
from aiohttp import web

from openapi_server.models.trips_trip_details200_response import TripsTripDetails200Response
from openapi_server import util


async def trips_trip_details_0(request: web.Request, track_token=None) -> web.Response:
    """Trips - trip details

    Trips - trip details

    :param track_token: 
    :type track_token: str

    """
    return web.Response(status=200)
