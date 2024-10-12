from typing import List, Dict
from aiohttp import web

from openapi_server.models.global_notification_setting import GlobalNotificationSetting
from openapi_server.models.put_v3_notification_settings_request import PutV3NotificationSettingsRequest
from openapi_server import util


async def get_v3_notification_settings(request: web.Request, ) -> web.Response:
    """Get global notification level settings and email, defaults to Participate

    This feature was introduced in GitLab 8.12


    """
    return web.Response(status=200)


async def put_v3_notification_settings(request: web.Request, body=None) -> web.Response:
    """Update global notification level settings and email, defaults to Participate

    This feature was introduced in GitLab 8.12

    :param body: 
    :type body: dict | bytes

    """
    body = PutV3NotificationSettingsRequest.from_dict(body)
    return web.Response(status=200)
