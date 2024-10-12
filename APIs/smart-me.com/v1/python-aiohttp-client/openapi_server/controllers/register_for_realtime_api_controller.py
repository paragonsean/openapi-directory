from typing import List, Dict
from aiohttp import web

from openapi_server.models.register_realtime_api_data import RegisterRealtimeApiData
from openapi_server import util


async def register_for_realtime_api_delete(request: web.Request, id) -> web.Response:
    """Deletes a realtime API registration.

    Deletes a realtime API registration.

    :param id: The ID of the realtime API registration
    :type id: str

    """
    return web.Response(status=200)


async def register_for_realtime_api_get(request: web.Request, ) -> web.Response:
    """Gets all registrations for the Realtime API.

    Gets all registrations for the Realtime API.


    """
    return web.Response(status=200)


async def register_for_realtime_api_post(request: web.Request, body) -> web.Response:
    """Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud.               More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

    Creates a new registration for the realtime API. The Realtime API sends you the data of the registred devices as soon as we have them on the cloud. More Information about the realtime API: https://www.smart-me.com/Description/api/realtimeapi.aspx

    :param body: 
    :type body: dict | bytes

    """
    body = RegisterRealtimeApiData.from_dict(body)
    return web.Response(status=200)
