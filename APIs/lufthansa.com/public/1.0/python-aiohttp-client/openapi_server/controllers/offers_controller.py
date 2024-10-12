from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def offers_lounges_by_location_get(request: web.Request, location, accept, cabin_class=None, tier_code=None, lang=None) -> web.Response:
    """Lounges

    Lounge information

    :param location: 3-leter IATA airport or city code (e.g. &#39;ZRH&#39;)
    :type location: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param cabin_class: Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39; (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;)
    :type cabin_class: str
    :param tier_code: Frequent flyer level (&#39;FTL&#39;, &#39;SGC&#39;, &#39;SEN&#39;, &#39;HON&#39;) (Acceptable values are: \&quot;\&quot;, \&quot;FTL\&quot;, \&quot;SGC\&quot;, \&quot;SEN\&quot;, \&quot;HON\&quot;)
    :type tier_code: str
    :param lang: Language code.
    :type lang: str

    """
    return web.Response(status=200)


async def offers_seatmaps_destination_date_cabin_class_by_flight_number_and_origin_get(request: web.Request, flight_number, origin, destination, _date, cabin_class, accept) -> web.Response:
    """Seat Maps

    Cabin layout and seat characteristics.

    :param flight_number: Flight number including carrier code and any suffix (e.g. &#39;LH2037&#39;)
    :type flight_number: str
    :param origin: Departure airport. 3-letter IATA airport code (e.g. &#39;TXL&#39;)
    :type origin: str
    :param destination: Destination airport. 3-letter IATA airport code (e.g. &#39;MUC&#39;)
    :type destination: str
    :param _date: Departure date (YYYY-MM-DD)
    :type _date: str
    :param cabin_class: Cabin class: &#39;M&#39;, &#39;E&#39;, &#39;C&#39;, &#39;F&#39;. Some flights have fewer classes (Acceptable values are: \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;)
    :type cabin_class: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str

    """
    return web.Response(status=200)
