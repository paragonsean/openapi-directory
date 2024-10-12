from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_venues import JsonVenues
from openapi_server import util


async def resource10_search_venues_get_venues_get(request: web.Request, city_id=None, city_name=None, country=None, name=None, p=None, state=None, state_code=None) -> web.Response:
    """Search for venues.

    Search for venues.

    :param city_id: the city&#39;s geoId
    :type city_id: str
    :param city_name: name of the city where the venue is located
    :type city_name: str
    :param country: the city&#39;s country
    :type country: str
    :param name: name of the venue
    :type name: str
    :param p: the number of the result page you&#39;d like to have
    :type p: int
    :param state: the city&#39;s state
    :type state: str
    :param state_code: the city&#39;s state code
    :type state_code: str

    """
    return web.Response(status=200)
