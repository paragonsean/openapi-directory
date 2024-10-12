from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_statuses(request: web.Request, show_id) -> web.Response:
    """Gets the last 100 statuses for this show.

    For Twitter, statuses are synonymous with tweets.

    :param show_id: Unique ID for a show
    :type show_id: str

    """
    return web.Response(status=200)
