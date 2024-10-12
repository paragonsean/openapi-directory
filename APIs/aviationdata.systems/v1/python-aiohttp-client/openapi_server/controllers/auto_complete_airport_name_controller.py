from typing import List, Dict
from aiohttp import web

from openapi_server.models.airports_api_controllers_auto_complete_airport_name_controller_response import AirportsAPIControllersAutoCompleteAirportNameControllerResponse
from openapi_server import util


async def auto_complete_airport_name_airport_name_search(request: web.Request, airport_name, airport_service_type, optional_country_code=None) -> web.Response:
    """Autocomplete airport names. Returns a maximum of 10 airport names.

    Required parameters: airport_name, airport_service_type. Optional parameter: country code (ISO 3166-1).

    :param airport_name: Required: The airports name
    :type airport_name: str
    :param airport_service_type: Required: Needs to be: All, Scheduled or NonScheduled
    :type airport_service_type: str
    :param optional_country_code: Optional: Country code (ISO 3166-1). This can be found via /countries
    :type optional_country_code: str

    """
    return web.Response(status=200)
