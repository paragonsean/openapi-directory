from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_setting import ApplicationSetting
from openapi_server.models.put_v3_application_settings_request import PutV3ApplicationSettingsRequest
from openapi_server import util


async def get_v3_application_settings(request: web.Request, ) -> web.Response:
    """Get the current application settings

    Get the current application settings


    """
    return web.Response(status=200)


async def put_v3_application_settings(request: web.Request, body) -> web.Response:
    """Modify application settings

    Modify application settings

    :param body: 
    :type body: dict | bytes

    """
    body = PutV3ApplicationSettingsRequest.from_dict(body)
    return web.Response(status=200)
