from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_airport_details_controller_response import AirportsAPIControllersAirportDetailsControllerResponse
from openapi_server import util


async def airport_details_airport_name_search(request: web.Request, airport_name) -> web.Response:
    """Search for airport by name

    Required parameters: airport_name, api_mode

    :param airport_name: Required: The airports name
    :type airport_name: str

    """
    return web.Response(status=200)
