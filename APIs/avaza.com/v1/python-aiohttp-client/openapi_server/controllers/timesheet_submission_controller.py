from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def timesheet_submission_post(request: web.Request, send_notifications=None, whole_week_of=None, whole_day_of=None, user_id=None) -> web.Response:
    """Submit Timesheets for Approval.

    Either provide a a specific Day (WholeDayOf) or any day in a Week (WholeWeekOf) to submit all draft timesheets in that day or week

    :param send_notifications: Send email alerts to timesheet approvers. Defaults to true
    :type send_notifications: bool
    :param whole_week_of: A date (yyyy-MM-dd) that falls within  a Week to have all timesheets in that week submitted. Respects the First Day of Week setting in your account Timesheet Settings to determine the week range.
    :type whole_week_of: str
    :param whole_day_of: A date (yyyy-MM-dd) to submit all timesheets on this day
    :type whole_day_of: str
    :param user_id: The user to submit timesheets for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
    :type user_id: int

    """
    whole_week_of = util.deserialize_datetime(whole_week_of)
    whole_day_of = util.deserialize_datetime(whole_day_of)
    return web.Response(status=200)
