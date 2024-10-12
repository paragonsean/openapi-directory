from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.event_detail_settings import EventDetailSettings
from openapi_server.models.event_detail_settings_url import EventDetailSettingsUrl
from openapi_server import util


async def get_marketing_v3_marketing_events_app_id_settings_get_all(request: web.Request, app_id) -> web.Response:
    """Retrieve the application settings

    Retrieve the current settings for the application.

    :param app_id: The id of the application to retrieve the settings for.
    :type app_id: int

    """
    return web.Response(status=200)


async def post_marketing_v3_marketing_events_app_id_settings_create(request: web.Request, app_id, body) -> web.Response:
    """Update the application settings

    Create or update the current settings for the application.

    :param app_id: The id of the application to update the settings for.
    :type app_id: int
    :param body: The new application settings
    :type body: dict | bytes

    """
    body = EventDetailSettingsUrl.from_dict(body)
    return web.Response(status=200)
