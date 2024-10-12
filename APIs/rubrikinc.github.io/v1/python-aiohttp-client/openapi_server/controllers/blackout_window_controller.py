from typing import List, Dict
from aiohttp import web

from openapi_server.models.global_blackout_window_status import GlobalBlackoutWindowStatus
from openapi_server import util


async def get_blackout_window_status(request: web.Request, ) -> web.Response:
    """Get current status of global blackout window

    Determine whether global blackout window is currently active.


    """
    return web.Response(status=200)


async def toggle_blackout_window(request: web.Request, body) -> web.Response:
    """Starts or stops the global blackout window in local Rubrik cluster

    Returns whether or not the system is in a blackout window.

    :param body: Whether to start or stop the global blackout window.
    :type body: dict | bytes

    """
    body = GlobalBlackoutWindowStatus.from_dict(body)
    return web.Response(status=200)
