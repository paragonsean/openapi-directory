from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server.models.dnd_end_dnd_error_schema import DndEndDndErrorSchema
from openapi_server.models.dnd_end_dnd_schema import DndEndDndSchema
from openapi_server.models.dnd_end_snooze_error_schema import DndEndSnoozeErrorSchema
from openapi_server.models.dnd_end_snooze_schema import DndEndSnoozeSchema
from openapi_server.models.dnd_info_error_schema import DndInfoErrorSchema
from openapi_server.models.dnd_info_schema import DndInfoSchema
from openapi_server.models.dnd_set_snooze_error_schema import DndSetSnoozeErrorSchema
from openapi_server.models.dnd_set_snooze_schema import DndSetSnoozeSchema
from openapi_server import util


async def dnd_end_dnd(request: web.Request, token) -> web.Response:
    """dnd_end_dnd

    Ends the current user&#39;s Do Not Disturb session immediately.

    :param token: Authentication token. Requires scope: &#x60;dnd:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def dnd_end_snooze(request: web.Request, token) -> web.Response:
    """dnd_end_snooze

    Ends the current user&#39;s snooze mode immediately.

    :param token: Authentication token. Requires scope: &#x60;dnd:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def dnd_info(request: web.Request, token=None, user=None) -> web.Response:
    """dnd_info

    Retrieves a user&#39;s current Do Not Disturb status.

    :param token: Authentication token. Requires scope: &#x60;dnd:read&#x60;
    :type token: str
    :param user: User to fetch status for (defaults to current user)
    :type user: str

    """
    return web.Response(status=200)


async def dnd_set_snooze(request: web.Request, num_minutes, token) -> web.Response:
    """dnd_set_snooze

    Turns on Do Not Disturb mode for the current user, or changes its duration.

    :param num_minutes: Number of minutes, from now, to snooze until.
    :type num_minutes: str
    :param token: Authentication token. Requires scope: &#x60;dnd:write&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def dnd_team_info(request: web.Request, token=None, users=None) -> web.Response:
    """dnd_team_info

    Retrieves the Do Not Disturb status for up to 50 users on a team.

    :param token: Authentication token. Requires scope: &#x60;dnd:read&#x60;
    :type token: str
    :param users: Comma-separated list of users to fetch Do Not Disturb status for
    :type users: str

    """
    return web.Response(status=200)
