from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.price_ranges_entity import PriceRangesEntity
from openapi_server.models.venues_entity import VenuesEntity
from openapi_server import util


async def fetch_all_price_ranges(request: web.Request, label=None, show_ignored=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all price ranges

    

    :param label: Find only the price ranges whose label contains this value.
    :type label: str
    :param show_ignored: If set to &#x60;false&#x60;, show only the price ranges which are not ignored. If set to &#x60;true&#x60;, show all price ranges.
    :type show_ignored: bool
    :param sort: Sort the price ranges in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_one_price_range(request: web.Request, price_range_id, accept_language=None) -> web.Response:
    """Get one price range by ID

    

    :param price_range_id: ID of the targeted price range.
    :type price_range_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)
