from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_camera_video_settings_request import UpdateDeviceCameraVideoSettingsRequest
from openapi_server import util


async def get_device_camera_video_settings_1(request: web.Request, serial) -> web.Response:
    """Returns video settings for the given camera

    Returns video settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_camera_video_settings_1(request: web.Request, serial, body=None) -> web.Response:
    """Update video settings for the given camera

    Update video settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraVideoSettingsRequest.from_dict(body)
    return web.Response(status=200)
