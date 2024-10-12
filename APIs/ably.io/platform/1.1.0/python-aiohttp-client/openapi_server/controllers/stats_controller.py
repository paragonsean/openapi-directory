from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def get_stats(request: web.Request, x_ably_version=None, format=None, start=None, limit=None, end=None, direction=None, unit=None) -> web.Response:
    """Retrieve usage statistics for an application

    The Ably system can be queried to obtain usage statistics for a given application, and results are provided aggregated across all channels in use in the application in the specified period. Stats may be used to track usage against account quotas.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param start: 
    :type start: str
    :param limit: 
    :type limit: int
    :param end: 
    :type end: str
    :param direction: 
    :type direction: str
    :param unit: Specifies the unit of aggregation in the returned results.
    :type unit: str

    """
    return web.Response(status=200)


async def get_time(request: web.Request, x_ably_version=None, format=None) -> web.Response:
    """Get the service time

    This returns the service time in milliseconds since the epoch.

    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str

    """
    return web.Response(status=200)
