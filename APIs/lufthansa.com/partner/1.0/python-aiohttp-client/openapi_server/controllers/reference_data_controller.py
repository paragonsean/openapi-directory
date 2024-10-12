from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def seat_details(request: web.Request, aircraft_code, accept, cabin_code, lang=None) -> web.Response:
    """Seat Details

    A description of all available seat details by aircraft type. You can retrieve the full set or details for a particular aircraft type.

    :param aircraft_code: Aircraft type. 3-character IATA equipment code
    :type aircraft_code: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param cabin_code: Cabin class: M, E, C, F (Acceptable values are: \&quot;\&quot;, \&quot;M\&quot;, \&quot;E\&quot;, \&quot;C\&quot;, \&quot;F\&quot;)
    :type cabin_code: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str

    """
    return web.Response(status=200)
