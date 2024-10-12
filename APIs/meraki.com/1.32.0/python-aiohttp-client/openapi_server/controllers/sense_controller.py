from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_camera_sense_request import UpdateDeviceCameraSenseRequest
from openapi_server import util


async def get_device_camera_sense_1(request: web.Request, serial) -> web.Response:
    """Returns sense settings for a given camera

    Returns sense settings for a given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_sense_object_detection_models_1(request: web.Request, serial) -> web.Response:
    """Returns the MV Sense object detection model list for the given camera

    Returns the MV Sense object detection model list for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_camera_sense_1(request: web.Request, serial, body=None) -> web.Response:
    """Update sense settings for the given camera

    Update sense settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraSenseRequest.from_dict(body)
    return web.Response(status=200)
