from typing import List, Dict
from aiohttp import web

from openapi_server.models.schedule_assignment_list import ScheduleAssignmentList
from openapi_server import util


async def schedule_assignment_get(request: web.Request, updated_after=None, schedule_date_from=None, schedule_date_to=None, schedule_series_id=None, user_id=None, user_email=None, page_size=None, page_number=None, sort=None) -> web.Response:
    """Gets list of Schedule Assignments.

    Schedule assignments are per-day, and link to a parent Schedule Series.

    :param updated_after: Limit results to records updated after the specified date
    :type updated_after: str
    :param schedule_date_from: Filter for schedule assignement  that are  on or after a specific date
    :type schedule_date_from: str
    :param schedule_date_to: Filter for schedules that are on or before a specific date
    :type schedule_date_to: str
    :param schedule_series_id: Filter to records for a particular Schedule Series
    :type schedule_series_id: int
    :param user_id: The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
    :type user_id: int
    :param user_email: The email of the user who has been scheduled
    :type user_email: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    schedule_date_from = util.deserialize_datetime(schedule_date_from)
    schedule_date_to = util.deserialize_datetime(schedule_date_to)
    return web.Response(status=200)
