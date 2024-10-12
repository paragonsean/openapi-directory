from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.sandbox_driver_availability import SandboxDriverAvailability
from openapi_server.models.sandbox_primetime import SandboxPrimetime
from openapi_server.models.sandbox_ride_status import SandboxRideStatus
from openapi_server.models.sandbox_ride_type import SandboxRideType
from openapi_server.models.sandbox_ride_update import SandboxRideUpdate
from openapi_server import util


async def set_prime_time(request: web.Request, request) -> web.Response:
    """Preset Prime Time percentage

    Preset a Prime Time percentage in the region surrounding the specified location. This Prime Time percentage will be applied when requesting cost, or when requesting a ride in sandbox mode. 

    :param request: Prime Time to be preset in the region surrounding the lat, lng
    :type request: dict | bytes

    """
    request = SandboxPrimetime.from_dict(request)
    return web.Response(status=200)


async def set_ride_status(request: web.Request, id, request) -> web.Response:
    """Propagate ride through ride status

    Propagate a sandbox-ride through various ride status 

    :param id: The ID of the ride
    :type id: str
    :param request: status to propagate the ride into
    :type request: dict | bytes

    """
    request = SandboxRideStatus.from_dict(request)
    return web.Response(status=200)


async def set_ride_type_availability(request: web.Request, ride_type, request) -> web.Response:
    """Driver availability for processing ride request

    Set driver availability for the provided ride_type in the city/region surrounding the specified location 

    :param ride_type: 
    :type ride_type: str
    :param request: Driver availability to be preset in the region surrounding the lat, lng
    :type request: dict | bytes

    """
    request = SandboxDriverAvailability.from_dict(request)
    return web.Response(status=200)


async def set_ride_types(request: web.Request, request) -> web.Response:
    """Preset types of rides for sandbox

    The sandbox-ridetypes endpoint allows you to preset the ridetypes in the region surrounding the specified latitude and longitude to allow testing different scenarios 

    :param request: Ridetypes to be preset in the region surrounding the lat, lng
    :type request: dict | bytes

    """
    request = SandboxRideType.from_dict(request)
    return web.Response(status=200)
