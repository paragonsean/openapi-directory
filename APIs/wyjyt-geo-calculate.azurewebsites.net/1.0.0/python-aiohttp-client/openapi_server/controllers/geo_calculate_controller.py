from typing import List, Dict
from aiohttp import web

from openapi_server.models.geo_convert_request import GeoConvertRequest
from openapi_server.models.geo_convert_response import GeoConvertResponse
from openapi_server.models.geo_distance_request import GeoDistanceRequest
from openapi_server.models.geo_distance_response import GeoDistanceResponse
from openapi_server.models.geo_fence_request import GeoFenceRequest
from openapi_server.models.geo_fence_response import GeoFenceResponse
from openapi_server.models.geo_sky_request import GeoSkyRequest
from openapi_server.models.geo_sky_response import GeoSkyResponse
from openapi_server.models.wyjyt_error_response import WyjytErrorResponse
from openapi_server import util


async def convert(request: web.Request, body) -> web.Response:
    """Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

    Convert the list of geo coordinates to a standard format - (latlon | utm | mgrs | ecef | epsg3857 | georef | cartesian)

    :param body: 
    :type body: dict | bytes

    """
    body = GeoConvertRequest.from_dict(body)
    return web.Response(status=200)


async def distance(request: web.Request, body) -> web.Response:
    """Calculate the distance between two geo coordinates.

    Calculate the distance between two geo coordinates.

    :param body: 
    :type body: dict | bytes

    """
    body = GeoDistanceRequest.from_dict(body)
    return web.Response(status=200)


async def fence(request: web.Request, body) -> web.Response:
    """Check if a list of coordinates are inside of a fence of coordinates.

    Check if a list of coordinates are inside of a fence of coordinates.

    :param body: 
    :type body: dict | bytes

    """
    body = GeoFenceRequest.from_dict(body)
    return web.Response(status=200)


async def sky(request: web.Request, body) -> web.Response:
    """Calculate sun, moon, eclipse and sky information for the date and location.

    Calculate sun, moon, eclipse and sky information for the date and location.

    :param body: 
    :type body: dict | bytes

    """
    body = GeoSkyRequest.from_dict(body)
    return web.Response(status=200)
