from typing import List, Dict
from aiohttp import web

from openapi_server.models.reminders_add_error_schema import RemindersAddErrorSchema
from openapi_server.models.reminders_add_schema import RemindersAddSchema
from openapi_server.models.reminders_complete_error_schema import RemindersCompleteErrorSchema
from openapi_server.models.reminders_complete_schema import RemindersCompleteSchema
from openapi_server.models.reminders_delete_error_schema import RemindersDeleteErrorSchema
from openapi_server.models.reminders_delete_schema import RemindersDeleteSchema
from openapi_server.models.reminders_info_error_schema import RemindersInfoErrorSchema
from openapi_server.models.reminders_info_schema import RemindersInfoSchema
from openapi_server.models.reminders_list_error_schema import RemindersListErrorSchema
from openapi_server.models.reminders_list_schema import RemindersListSchema
from openapi_server import util


async def reminders_add(request: web.Request, token, text, time, user=None) -> web.Response:
    """reminders_add

    Creates a reminder.

    :param token: Authentication token. Requires scope: &#x60;reminders:write&#x60;
    :type token: str
    :param text: The content of the reminder
    :type text: str
    :param time: When this reminder should happen: the Unix timestamp (up to five years from now), the number of seconds until the reminder (if within 24 hours), or a natural language description (Ex. \\\&quot;in 15 minutes,\\\&quot; or \\\&quot;every Thursday\\\&quot;)
    :type time: str
    :param user: The user who will receive the reminder. If no user is specified, the reminder will go to user who created it.
    :type user: str

    """
    return web.Response(status=200)


async def reminders_complete(request: web.Request, token=None, reminder=None) -> web.Response:
    """reminders_complete

    Marks a reminder as complete.

    :param token: Authentication token. Requires scope: &#x60;reminders:write&#x60;
    :type token: str
    :param reminder: The ID of the reminder to be marked as complete
    :type reminder: str

    """
    return web.Response(status=200)


async def reminders_delete(request: web.Request, token=None, reminder=None) -> web.Response:
    """reminders_delete

    Deletes a reminder.

    :param token: Authentication token. Requires scope: &#x60;reminders:write&#x60;
    :type token: str
    :param reminder: The ID of the reminder
    :type reminder: str

    """
    return web.Response(status=200)


async def reminders_info(request: web.Request, token=None, reminder=None) -> web.Response:
    """reminders_info

    Gets information about a reminder.

    :param token: Authentication token. Requires scope: &#x60;reminders:read&#x60;
    :type token: str
    :param reminder: The ID of the reminder
    :type reminder: str

    """
    return web.Response(status=200)


async def reminders_list(request: web.Request, token=None) -> web.Response:
    """reminders_list

    Lists all reminders created by or for a given user.

    :param token: Authentication token. Requires scope: &#x60;reminders:read&#x60;
    :type token: str

    """
    return web.Response(status=200)
