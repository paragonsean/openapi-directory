from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_v1_deactivation import MessagingV1Deactivation
from openapi_server import util


async def fetch_deactivation(request: web.Request, _date=None) -> web.Response:
    """fetch_deactivation

    Fetch a list of all United States numbers that have been deactivated on a specific date.

    :param _date: The request will return a list of all United States Phone Numbers that were deactivated on the day specified by this parameter. This date should be specified in YYYY-MM-DD format.
    :type _date: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)
