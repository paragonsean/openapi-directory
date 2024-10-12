from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_airport_iata_controller_response import AirportsAPIControllersAirportIATAControllerResponse
from openapi_server import util


async def airport_iata_airport_iata_search(request: web.Request, airport_iata) -> web.Response:
    """Search for airport by IATA code

    Required parameters: airport_iata

    :param airport_iata: Required: The airports IATA code
    :type airport_iata: str

    """
    return web.Response(status=200)
