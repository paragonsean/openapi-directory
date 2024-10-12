from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_country_list_controller_country_list_response import AirportsAPIControllersCountryListControllerCountryListResponse
from openapi_server import util


async def country_list_country_airport_list(request: web.Request, ) -> web.Response:
    """Country list. Returns a list of countries where airport data is available

    


    """
    return web.Response(status=200)
