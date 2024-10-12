from typing import List, Dict
from aiohttp import web

from openapi_server.models.error400 import Error400
from openapi_server.models.error401 import Error401
from openapi_server.models.error500 import Error500
from openapi_server.models.success_sentiments import SuccessSentiments
from openapi_server import util


async def get_sentiments_by_hotel_ids(request: web.Request, hotel_ids) -> web.Response:
    """Get sentiments by Amadeus Hotel Ids

    

    :param hotel_ids: Comma-separated list of Amadeus Hotel Ids (max. 3) . Amadeus Hotel Ids are found in the Hotel Search response (parameter name is &#39;hotelId&#39;).
    :type hotel_ids: List[str]

    """
    return web.Response(status=200)
