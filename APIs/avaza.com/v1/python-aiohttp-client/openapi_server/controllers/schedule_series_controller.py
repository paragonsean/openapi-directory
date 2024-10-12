from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_booking import CreateBooking
from openapi_server.models.create_leave import CreateLeave
from openapi_server.models.edit_booking import EditBooking
from openapi_server.models.edit_leave import EditLeave
from openapi_server.models.schedule_series_details import ScheduleSeriesDetails
from openapi_server.models.schedule_series_list import ScheduleSeriesList
from openapi_server import util


async def schedule_series_add_booking(request: web.Request, model) -> web.Response:
    """Create new Schedule Booking

    

    :param model: 
    :type model: dict | bytes

    """
    model = CreateBooking.from_dict(model)
    return web.Response(status=200)


async def schedule_series_add_leave(request: web.Request, model) -> web.Response:
    """Create new Leave Booking

    

    :param model: 
    :type model: dict | bytes

    """
    model = CreateLeave.from_dict(model)
    return web.Response(status=200)


async def schedule_series_edit_booking(request: web.Request, model) -> web.Response:
    """Edit Booking

    

    :param model: 
    :type model: dict | bytes

    """
    model = EditBooking.from_dict(model)
    return web.Response(status=200)


async def schedule_series_edit_leave(request: web.Request, model) -> web.Response:
    """Edit Leave Booking

    

    :param model: 
    :type model: dict | bytes

    """
    model = EditLeave.from_dict(model)
    return web.Response(status=200)


async def schedule_series_get(request: web.Request, updated_after=None, schedule_start_date_from=None, schedule_start_date_to=None, schedule_end_date_from=None, schedule_end_date_to=None, user_id=None, user_email=None, time_sheet_category_id=None, time_sheet_category_name=None, leave_type_id=None, project_id=None, company_id=None, page_size=None, page_number=None, sort=None) -> web.Response:
    """Gets list of Schedule Series

    Schedule Series represents a strip of time assigned to a user over a date range, for a certain number of hours per day. They can be for Leave or for project work Bookings.

    :param updated_after: Limit results to records updated after the specified date
    :type updated_after: str
    :param schedule_start_date_from: Filter for schedules that start on or after a specific date
    :type schedule_start_date_from: str
    :param schedule_start_date_to: Filter for schedules that start on or before a specific date
    :type schedule_start_date_to: str
    :param schedule_end_date_from: Filter for schedules that end on or after a specific date
    :type schedule_end_date_from: str
    :param schedule_end_date_to: Filter for schedules that end on or before a specific date
    :type schedule_end_date_to: str
    :param user_id: The UserID of a schedule user to filter assignments for. Only api users with Admin role can see all schedules across all users. Users with ScheduleUser role can access their own ScheduleSeries.
    :type user_id: int
    :param user_email: The email of the user who has been scheduled
    :type user_email: str
    :param time_sheet_category_id: Filter for schedule records linked to a specific timesheeet category
    :type time_sheet_category_id: int
    :param time_sheet_category_name: Filter for schedule records with a specific timesheeet category name (exact string match)
    :type time_sheet_category_name: str
    :param leave_type_id: Filter to records of a particular leave type
    :type leave_type_id: int
    :param project_id: Filter to only include books linked to a specific project
    :type project_id: int
    :param company_id: Filter to only include records linked to projects, where that project belongs to a specific customer company
    :type company_id: int
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    schedule_start_date_from = util.deserialize_datetime(schedule_start_date_from)
    schedule_start_date_to = util.deserialize_datetime(schedule_start_date_to)
    schedule_end_date_from = util.deserialize_datetime(schedule_end_date_from)
    schedule_end_date_to = util.deserialize_datetime(schedule_end_date_to)
    return web.Response(status=200)
