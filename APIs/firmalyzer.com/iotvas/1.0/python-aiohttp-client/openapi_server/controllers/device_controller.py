from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_features import DeviceFeatures
from openapi_server.models.device_info import DeviceInfo
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def detect_device(request: web.Request, body) -> web.Response:
    """Detect iot device by service banners and mac address

    Use device service banners and mac address captured by your network port scanner, vulnerability assessment or asset discovery tools to detect device maker, model and firmware information

    :param body: 
    :type body: dict | bytes

    """
    body = DeviceFeatures.from_dict(body)
    return web.Response(status=200)
