from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_country_airport_list_controller_airport_list_response import AirportsAPIControllersCountryAirportListControllerAirportListResponse
from openapi_server import util


async def country_airport_list_country_airport_list(request: web.Request, country_code, airport_service_type) -> web.Response:
    """Country airports. Returns a list of airports for a country code(ISO 3166-1 alpha-2 code)

    Required parameters: country code (ISO 3166-1), airport_service_type.

    :param country_code: Country code (ISO 3166-1). This can be found via /countries
    :type country_code: str
    :param airport_service_type: Required: Needs to be: All, Scheduled or NonScheduled
    :type airport_service_type: str

    """
    return web.Response(status=200)
