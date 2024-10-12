from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def event_api_get_list(request: web.Request, min_date=None, max_date=None, page=None, page_size=None, type_id=None, order_id=None) -> web.Response:
    """Get a list of all events optionally filtered by date. This request is extra throttled to 2 calls per page per hour.

    

    :param min_date: Specifies the oldest date to include in the response
    :type min_date: str
    :param max_date: Specifies the newest date to include in the response
    :type max_date: str
    :param page: Specifies the page to request
    :type page: int
    :param page_size: Specifies the pagesize. Defaults to 50, max value is 250
    :type page_size: int
    :param type_id: Filter for specific event types
    :type type_id: List[int]
    :param order_id: Filter for specific order id
    :type order_id: int

    """
    min_date = util.deserialize_datetime(min_date)
    max_date = util.deserialize_datetime(max_date)
    return web.Response(status=200)
