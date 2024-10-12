from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_endpoints_airport_response import ApiEndpointsAirportResponse
from openapi_server import util


async def airport_api_get_airport(request: web.Request, icao_code) -> web.Response:
    """airport_api_get_airport

    

    :param icao_code: 
    :type icao_code: str

    """
    return web.Response(status=200)
