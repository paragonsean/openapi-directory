from typing import List, Dict
from aiohttp import web

from openapi_server.models.airport_details_dto import AirportDetailsDto
from openapi_server.models.airport_dto import AirportDto
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.internal_server_error_response import InternalServerErrorResponse
from openapi_server.models.nearest_airport_dto import NearestAirportDto
from openapi_server import util


async def call58d8bcb7a9e6240e200cff24(request: web.Request, ) -> web.Response:
    """All airports

    Retrieve all airports.


    """
    return web.Response(status=200)


async def call58d8bcb7a9e6240e200cff25(request: web.Request, id) -> web.Response:
    """Airport by id.

    Retrieve airport by id.

    :param id: Airport code (3-character IATA code).
    :type id: str

    """
    return web.Response(status=200)


async def call58d8bcb8a9e6240e200cff26(request: web.Request, country_code) -> web.Response:
    """Airport(s) by country code.

    Retrieve airports by country code.

    :param country_code: Comma-separated list of country codes (2-character ISO 3166-1). More than 3 country codes is not allowed.
    :type country_code: str

    """
    return web.Response(status=200)


async def call58d8bcb8a9e6240e200cff27(request: web.Request, latitude=None, longitude=None, max_distance_in_km=None, limit=None) -> web.Response:
    """Nearest airport(s) by geo coordinates.

    Retrieve nearest airports by geo coordinates (latitude/longitude).

    :param latitude: Latitude in decimals, lower than -90.0 and higher than 90.0 is not allowed.
    :type latitude: str
    :param longitude: Longitude in decimals, lower than -180.0 and higher than 180.0 is not allowed.
    :type longitude: str
    :param max_distance_in_km: Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
    :type max_distance_in_km: str
    :param limit: Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
    :type limit: str

    """
    return web.Response(status=200)


async def call58d8bcb8a9e6240e200cff28(request: web.Request, id, max_distance_in_km=None, limit=None) -> web.Response:
    """Nearest airport(s) by airport id.

    Retrieve nearest airports by station id.

    :param id: Airport (IATA code) to search nearest airports for.
    :type id: str
    :param max_distance_in_km: Maximum distance in kilometers, lower than 1 and higher than 500 is not allowed. If not set, max value is applied.
    :type max_distance_in_km: str
    :param limit: Limits the result, lower than 0 is not allowed. If not set, the result is not limited.
    :type limit: str

    """
    return web.Response(status=200)
