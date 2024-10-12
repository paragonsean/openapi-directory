from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def timesheet_timer_get_running_timer(request: web.Request, user_id=None) -> web.Response:
    """Gets the  Running Timer if there is one for a user.

    

    :param user_id: Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    :type user_id: int

    """
    return web.Response(status=200)


async def timesheet_timer_start_timer(request: web.Request, id, user_id=None) -> web.Response:
    """Starts a Timer running on an existing Timesheet Entry

    

    :param id: id of timesheet entry that should be used as the basis for running a timer. If the existing timesheet is not on the current day, or you have start/end times enabled, then a new timesheet will be created for the timer.
    :type id: int
    :param user_id: Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    :type user_id: int

    """
    return web.Response(status=200)


async def timesheet_timer_stop_timer(request: web.Request, id, user_id=None) -> web.Response:
    """Stop the timer running on an existing Timesheet Entry

    

    :param id: The ID of the existing timesheet entry that needs its timer stopped
    :type id: int
    :param user_id: Optional - User ID number if impersonating a different user. Otherwise assumes the current user. Only users with certain security roles have permission to impersonate other users
    :type user_id: int

    """
    return web.Response(status=200)
