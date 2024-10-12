from typing import List, Dict
from aiohttp import web

from openapi_server.models.step import Step
from openapi_server.models.trip import Trip
from openapi_server import util


async def trip_get(request: web.Request, ) -> web.Response:
    """trip_get

    list user&#39;s trips


    """
    return web.Response(status=200)


async def trip_trip_id_stop_get(request: web.Request, trip_id) -> web.Response:
    """trip_trip_id_stop_get

    list stops for a trip identified by {trip_id}

    :param trip_id: id of the trip
    :type trip_id: str

    """
    return web.Response(status=200)
