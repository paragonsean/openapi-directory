from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_camera_quality_and_retention_request import UpdateDeviceCameraQualityAndRetentionRequest
from openapi_server import util


async def get_device_camera_quality_and_retention_1(request: web.Request, serial) -> web.Response:
    """Returns quality and retention settings for the given camera

    Returns quality and retention settings for the given camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_camera_quality_and_retention_1(request: web.Request, serial, body=None) -> web.Response:
    """Update quality and retention settings for the given camera

    Update quality and retention settings for the given camera

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCameraQualityAndRetentionRequest.from_dict(body)
    return web.Response(status=200)
