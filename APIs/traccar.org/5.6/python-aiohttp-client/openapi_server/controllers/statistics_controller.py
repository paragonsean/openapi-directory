from typing import List, Dict
from aiohttp import web

from openapi_server.models.statistics import Statistics
from openapi_server import util


async def statistics_get(request: web.Request, _from, to) -> web.Response:
    """Fetch server Statistics

    

    :param _from: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type _from: str
    :param to: in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60;
    :type to: str

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)
