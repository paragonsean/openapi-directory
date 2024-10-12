from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_camera_video_link_1(request: web.Request, serial, timestamp=None) -> web.Response:
    """Returns video link to the specified camera

    Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.

    :param serial: 
    :type serial: str
    :param timestamp: [optional] The video link will start at this time. The timestamp should be a string in ISO8601 format. If no timestamp is specified, we will assume current time.
    :type timestamp: str

    """
    timestamp = util.deserialize_datetime(timestamp)
    return web.Response(status=200)
