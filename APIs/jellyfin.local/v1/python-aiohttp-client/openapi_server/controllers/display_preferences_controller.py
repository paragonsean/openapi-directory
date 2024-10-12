from typing import List, Dict
from aiohttp import web

from openapi_server.models.display_preferences_dto import DisplayPreferencesDto
from openapi_server import util


async def get_display_preferences(request: web.Request, display_preferences_id, user_id, client) -> web.Response:
    """Get Display Preferences.

    

    :param display_preferences_id: Display preferences id.
    :type display_preferences_id: str
    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param client: Client.
    :type client: str

    """
    return web.Response(status=200)


async def update_display_preferences(request: web.Request, display_preferences_id, user_id, client, body) -> web.Response:
    """Update Display Preferences.

    

    :param display_preferences_id: Display preferences id.
    :type display_preferences_id: str
    :param user_id: User Id.
    :type user_id: str
    :type user_id: str
    :param client: Client.
    :type client: str
    :param body: New Display Preferences object.
    :type body: dict | bytes

    """
    body = DisplayPreferencesDto.from_dict(body)
    return web.Response(status=200)
