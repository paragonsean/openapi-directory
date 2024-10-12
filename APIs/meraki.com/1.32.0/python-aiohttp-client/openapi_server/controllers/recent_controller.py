from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_camera_analytics_recent_2(request: web.Request, serial, object_type=None) -> web.Response:
    """Returns most recent record for analytics zones

    Returns most recent record for analytics zones

    :param serial: 
    :type serial: str
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)
