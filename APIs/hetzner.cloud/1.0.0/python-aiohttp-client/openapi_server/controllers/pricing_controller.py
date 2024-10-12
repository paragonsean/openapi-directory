from typing import List, Dict
from aiohttp import web

from openapi_server.models.pricing_get200_response import PricingGet200Response
from openapi_server import util


async def pricing_get(request: web.Request, ) -> web.Response:
    """Get all prices

    Returns prices for all resources available on the platform. VAT and currency of the Project owner are used for calculations.  Both net and gross prices are included in the response. 


    """
    return web.Response(status=200)
