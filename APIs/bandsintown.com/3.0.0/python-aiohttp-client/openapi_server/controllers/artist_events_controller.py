from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_data import EventData
from openapi_server import util


async def artist_events(request: web.Request, artistname, app_id, _date=None) -> web.Response:
    """Get upcoming, past, or all artist events, or events within a date range

    artist events 

    :param artistname: The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C
    :type artistname: str
    :param app_id: The application ID assigned to you by Bandsintown
    :type app_id: str
    :param _date: Can be one of the following values: \&quot;upcoming\&quot;, \&quot;past\&quot;, \&quot;all\&quot;, or a date range e.g. \&quot;2015-05-05,2017-05-05\&quot;. If not specified, only upcoming shows are returned
    :type _date: str

    """
    return web.Response(status=200)
