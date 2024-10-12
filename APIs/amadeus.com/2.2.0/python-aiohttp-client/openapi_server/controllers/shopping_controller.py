from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error500 import Error500
from openapi_server.models.get_flight_offers_query import GetFlightOffersQuery
from openapi_server.models.success import Success
from openapi_server.models.success1 import Success1
from openapi_server import util


async def get_flight_offers(request: web.Request, origin_location_code, destination_location_code, departure_date, adults, return_date=None, children=None, infants=None, travel_class=None, included_airline_codes=None, excluded_airline_codes=None, non_stop=None, currency_code=None, max_price=None, max=None) -> web.Response:
    """Return list of Flight Offers based on searching criteria.

    

    :param origin_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) from which the traveler will depart, e.g. BOS for Boston
    :type origin_location_code: str
    :param destination_location_code: city/airport [IATA code](http://www.iata.org/publications/Pages/code-search.aspx) to which the traveler is going, e.g. PAR for Paris
    :type destination_location_code: str
    :param departure_date: the date on which the traveler will depart from the origin to go to the destination. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25
    :type departure_date: str
    :param adults: the number of adult travelers (age 12 or older on date of departure).
    :type adults: int
    :param return_date: the date on which the traveler will depart from the destination to return to the origin. If this parameter is not specified, only one-way itineraries are found. If this parameter is specified, only round-trip itineraries are found. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2018-02-28
    :type return_date: str
    :param children: the number of child travelers (older than age 2 and younger than age 12 on date of departure) who will each have their own separate seat. If specified, this number should be greater than or equal to 0
    :type children: int
    :param infants: the number of infant travelers (whose age is less or equal to 2 on date of departure). Infants travel on the lap of an adult traveler, and thus the number of infants must not exceed the number of adults. If specified, this number should be greater than or equal to 0
    :type infants: int
    :param travel_class: most of the flight time should be spent in a cabin of this quality or higher. The accepted travel class is economy, premium economy, business or first class. If no travel class is specified, the search considers any travel class
    :type travel_class: str
    :param included_airline_codes: This option ensures that the system will only consider these airlines. This can not be cumulated with parameter excludedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X 
    :type included_airline_codes: str
    :param excluded_airline_codes: This option ensures that the system will ignore these airlines. This can not be cumulated with parameter includedAirlineCodes.  Airlines are specified as [IATA airline codes](http://www.iata.org/publications/Pages/code-search.aspx) and are comma-separated, e.g. 6X,7X,8X 
    :type excluded_airline_codes: str
    :param non_stop: if set to true, the search will find only flights going from the origin to the destination with no stop in between
    :type non_stop: bool
    :param currency_code: the preferred currency for the flight offers. Currency is specified in the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) format, e.g. EUR for Euro
    :type currency_code: str
    :param max_price: maximum price per traveler. By default, no limit is applied. If specified, the value should be a positive number with no decimals
    :type max_price: int
    :param max: maximum number of flight offers to return. If specified, the value should be greater than or equal to 1
    :type max: int

    """
    departure_date = util.deserialize_date(departure_date)
    return_date = util.deserialize_date(return_date)
    return web.Response(status=200)


async def search_flight_offers(request: web.Request, x_http_method_override, body) -> web.Response:
    """Return list of Flight Offers based on posted searching criteria.

    

    :param x_http_method_override: the HTTP method to apply
    :type x_http_method_override: str
    :param body: list of criteria to retrieve a list of flight offers
    :type body: dict | bytes

    """
    body = GetFlightOffersQuery.from_dict(body)
    return web.Response(status=200)
