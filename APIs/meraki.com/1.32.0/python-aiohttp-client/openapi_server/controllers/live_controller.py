from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_camera_analytics_live_2(request: web.Request, serial) -> web.Response:
    """Returns live state from camera of analytics zones

    Returns live state from camera of analytics zones

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
