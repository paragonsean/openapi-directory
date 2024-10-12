from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_upsell_query import GetUpsellQuery
from openapi_server.models.success_upsell import SuccessUpsell
from openapi_server import util


async def upsell_air_offers(request: web.Request, x_http_method_override, upsell_flight_offers_body) -> web.Response:
    """Return a list of upsell Flight Offers based on given Flight Offers

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param upsell_flight_offers_body: list of criteria to upsell a dedicated flight-offers
    :type upsell_flight_offers_body: dict | bytes

    """
    upsell_flight_offers_body = GetUpsellQuery.from_dict(upsell_flight_offers_body)
    return web.Response(status=200)
