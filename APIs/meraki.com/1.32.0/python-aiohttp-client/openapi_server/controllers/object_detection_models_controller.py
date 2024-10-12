from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_camera_sense_object_detection_models_2(request: web.Request, serial) -> web.Response:
    """Returns the MV Sense object detection model list for the given camera

    Returns the MV Sense object detection model list for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
