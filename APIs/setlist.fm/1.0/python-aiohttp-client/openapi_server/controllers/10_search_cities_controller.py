from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_cities import JsonCities
from openapi_server import util


async def resource10_search_cities_get_cities_get(request: web.Request, country=None, name=None, p=None, state=None, state_code=None) -> web.Response:
    """Search for a city.

    Search for a city.

    :param country: the city&#39;s country
    :type country: str
    :param name: name of the city
    :type name: str
    :param p: the number of the result page you&#39;d like to have
    :type p: int
    :param state: state the city lies in
    :type state: str
    :param state_code: state code the city lies in
    :type state_code: str

    """
    return web.Response(status=200)
