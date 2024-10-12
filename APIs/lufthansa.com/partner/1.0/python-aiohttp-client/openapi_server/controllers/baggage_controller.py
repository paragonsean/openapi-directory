from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def baggage_trip_and_contact(request: web.Request, search_id, accept) -> web.Response:
    """Baggage Trip and Contact

    Retrieve passenger trip, contact and baggage details. This service is only accessible for LH privileged partners

    :param search_id: Bag tag number, PNR, boarding card or FQTV ID
    :type search_id: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str

    """
    return web.Response(status=200)
