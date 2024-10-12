from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.cost_estimate_response import CostEstimateResponse
from openapi_server.models.eta_estimate_response import EtaEstimateResponse
from openapi_server.models.nearby_drivers_response import NearbyDriversResponse
from openapi_server.models.ride_types_response import RideTypesResponse
from openapi_server import util


async def get_cost(request: web.Request, start_lat, start_lng, ride_type=None, end_lat=None, end_lng=None) -> web.Response:
    """Cost estimates

    Estimate the cost of taking a Lyft between two points. 

    :param start_lat: Latitude of the starting location
    :type start_lat: float
    :param start_lng: Longitude of the starting location
    :type start_lng: float
    :param ride_type: ID of a ride type
    :type ride_type: str
    :param end_lat: Latitude of the ending location
    :type end_lat: float
    :param end_lng: Longitude of the ending location
    :type end_lng: float

    """
    return web.Response(status=200)


async def get_drivers(request: web.Request, lat, lng) -> web.Response:
    """Available drivers nearby

    The drivers endpoint returns a list of nearby drivers&#39; lat and lng at a given location. 

    :param lat: Latitude of a location
    :type lat: float
    :param lng: Longitude of a location
    :type lng: float

    """
    return web.Response(status=200)


async def get_eta(request: web.Request, lat, lng, destination_lat=None, destination_lng=None, ride_type=None) -> web.Response:
    """Pickup ETAs

    The ETA endpoint lets you know how quickly a Lyft driver can come get you 

    :param lat: Latitude of a location
    :type lat: float
    :param lng: Longitude of a location
    :type lng: float
    :param destination_lat: Latitude of destination location
    :type destination_lat: float
    :param destination_lng: Longitude of destination location
    :type destination_lng: float
    :param ride_type: ID of a ride type
    :type ride_type: str

    """
    return web.Response(status=200)


async def get_ride_types(request: web.Request, lat, lng, ride_type=None) -> web.Response:
    """Types of rides

    The ride types endpoint returns information about what kinds of Lyft rides you can request at a given location. 

    :param lat: Latitude of a location
    :type lat: float
    :param lng: Longitude of a location
    :type lng: float
    :param ride_type: ID of a ride type
    :type ride_type: str

    """
    return web.Response(status=200)
