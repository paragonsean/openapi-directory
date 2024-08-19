from typing import List, Dict
from aiohttp import web

from openapi_server.models.near_earth_object_list import NearEarthObjectList
from openapi_server import util


async def retrieve_near_earth_object_feed(request: web.Request, start_date=None, end_date=None, detailed=None) -> web.Response:
    """Find Near Earth Objects by date

    Get a list of Near Earth Objects within a date range, The max range in one query is 7 days

    :param start_date: Start of date range search, format: yyyy-MM-dd - (ex: 2015-04-28)
    :type start_date: str
    :param end_date: End of date range search, format: yyyy-MM-dd - (ex: 2015-04-28). If left off search will extends 7 days from start_date
    :type end_date: str
    :param detailed: detailed
    :type detailed: bool

    """
    return web.Response(status=200)


async def retrieve_neo_feed_today(request: web.Request, detailed=None) -> web.Response:
    """Find Near Earth Objects for today

    Get a list of Near Earth Objects for today

    :param detailed: detailed
    :type detailed: bool

    """
    return web.Response(status=200)
