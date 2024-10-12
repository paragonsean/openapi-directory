from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success import Success
from openapi_server import util


async def get_air_traffic(request: web.Request, city_code, period, direction=None) -> web.Response:
    """Returns a list of air traffic reports.

    

    :param city_code: Code for the city following IATA standard. [IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx) - e.g. BOS for Boston
    :type city_code: str
    :param period: time period (year) of the statistics.  Year for which the statistic are requested following [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) 
    :type period: str
    :param direction: Use ARRIVING to have statistics on travelers coming to the city or DEPARTING for statistics on travelers leaving the city.  By default, statistics are given on travelers ARRIVING the city. 
    :type direction: str

    """
    return web.Response(status=200)
