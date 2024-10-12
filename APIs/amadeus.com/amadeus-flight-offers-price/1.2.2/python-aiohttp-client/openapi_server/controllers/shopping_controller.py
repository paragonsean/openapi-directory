from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_price_query import GetPriceQuery
from openapi_server.models.success_pricing import SuccessPricing
from openapi_server import util


async def quote_air_offers(request: web.Request, x_http_method_override, price_flight_offers_body, include=None, force_class=None) -> web.Response:
    """Confirm pricing of given flightOffers.

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param price_flight_offers_body: list of criteria to confirm the price of a dedicated flight-offers
    :type price_flight_offers_body: dict | bytes
    :param include: Sub-resources to be included:  * **credit-card-fees** to get the credit card fee applied on the booking  * **bags** to get extra bag options  * **other-services** to get services options  * **detailed-fare-rules** to get detailed fare rules options 
    :type include: List[str]
    :param force_class: parameter to force the usage of booking class for pricing - **true**, to for pricing with the specified booking class - **false**, to get the best available price 
    :type force_class: bool

    """
    price_flight_offers_body = GetPriceQuery.from_dict(price_flight_offers_body)
    return web.Response(status=200)
