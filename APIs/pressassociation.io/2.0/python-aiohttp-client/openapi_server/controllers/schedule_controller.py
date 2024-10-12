from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def list_schedule(request: web.Request, channel_id, start, end=None, aliases=None) -> web.Response:
    """Schedule Collection

    The schedule endpoint produces a linear TV schedule for a given channel and date range.   - The date range supplied must be no larger than 21 days.  - If no end data is passed the API will default to start date + 24 hours.

    :param channel_id: The identifier for the selected channel.
    :type channel_id: str
    :param start: The Start Date for the schedule.
    :type start: str
    :param end: The End Date for the schedule.
    :type end: str
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)
