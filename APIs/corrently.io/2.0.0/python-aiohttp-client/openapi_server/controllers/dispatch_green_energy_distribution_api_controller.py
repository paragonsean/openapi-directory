from typing import List, Dict
from aiohttp import web

from openapi_server.models.gsi_dispatch200_response import GsiDispatch200Response
from openapi_server import util


async def gsi_dispatch_0(request: web.Request, zip=None, key=None) -> web.Response:
    """Dispatch (Green Energy Distribution Schedule)

    Dispatch of green energy has two aspects to consider:   - Availability of gerneration facility (depends on weather and installed capacity)   - Demand of energy Using the green power index (GrünstromIndex) we have received a tool to automate distribution of energy in order to prevent redispatch situations. Doing this alows to opimize resource usage (tactical) and leverage data for investment planning (strategic). 

    :param zip: Zipcode (Postleitzahl) of a city in Germany.
    :type zip: str
    :param key: Any valid Stromkonto account (address).
    :type key: str

    """
    return web.Response(status=200)
