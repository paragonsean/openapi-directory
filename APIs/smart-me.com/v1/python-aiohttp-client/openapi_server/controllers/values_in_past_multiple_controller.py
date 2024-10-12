from typing import List, Dict
from aiohttp import web

from openapi_server.models.values_data import ValuesData
from openapi_server import util


async def values_in_past_multiple_get(request: web.Request, id, start_date, end_date, interval) -> web.Response:
    """Gets multiple values of a device. This call needs a smart-me professional licence.

    

    :param id: The ID of the device
    :type id: str
    :param start_date: The date when the first value should start
    :type start_date: str
    :param end_date: The date when the last value should start
    :type end_date: str
    :param interval: The interval in minutes betwenn the values. 0 means as fast as possible. Only 1000 values can be get in one call.
    :type interval: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
