from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_stored_alerts(request: web.Request, thing, key, _date, hour=None, response_type=None) -> web.Response:
    """Read all the saved alerts for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str
    :param _date: The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day.
    :type _date: str
    :param hour: The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
    :type hour: str
    :param response_type: Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
    :type response_type: str

    """
    return web.Response(status=200)


async def get_stored_dweets_for_thing_get(request: web.Request, thing, key, _date, hour=None, response_type=None) -> web.Response:
    """Read all the saved dweets for a thing from long term storage.  You can query a maximum of 1 day per request and a granularly of 1 hour.

    

    :param thing: A unique name of a thing.
    :type thing: str
    :param key: A valid key for a locked thing. If the thing is not locked, this can be ignored.
    :type key: str
    :param _date: The calendar date (YYYY-MM-DD) from which you&#39;d like to start your query.  The response will be a maximum of one day.
    :type _date: str
    :param hour: The hour of the day represented in the date parameter in 24-hour (00-23) format.  If this parameter is included, a maximum of 1 hour will be returned starting at this hour.
    :type hour: str
    :param response_type: Current valid parameters for this are &#39;csv&#39; and &#39;json&#39;.  If this parameter is left blank, all responses default to hapi-json dweet-speak.
    :type response_type: str

    """
    return web.Response(status=200)
