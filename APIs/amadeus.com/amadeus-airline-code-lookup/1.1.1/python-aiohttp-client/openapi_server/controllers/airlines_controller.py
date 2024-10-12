from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.success_things import SuccessThings
from openapi_server import util


async def getairlines(request: web.Request, airline_codes=None) -> web.Response:
    """Return airlines information.

    

    :param airline_codes: Code of the airline following IATA standard([IATA table codes](http://www.iata.org/publications/Pages/code-search.aspx)) or ICAO standard ([ICAO airlines table codes](https://en.wikipedia.org/wiki/List_of_airline_codes))  Several airlines can be selected at once by sending a list separated by a coma (i.e. AF, SWA) 
    :type airline_codes: str

    """
    return web.Response(status=200)
