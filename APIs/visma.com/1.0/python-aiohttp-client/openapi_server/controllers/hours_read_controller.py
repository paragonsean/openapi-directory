from typing import List, Dict
from aiohttp import web

from openapi_server.models.billable_status_type import BillableStatusType
from openapi_server.models.deleted_work_hour_model import DeletedWorkHourModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.time_entry_model import TimeEntryModel
from openapi_server.models.work_hour_output_model import WorkHourOutputModel
from openapi_server import util


async def time_entries_get_time_entries(request: web.Request, first_row=None, phase_guid=None, time_entry_type_guid=None, row_count=None, changed_since=None) -> web.Response:
    """Get the time entries.

    

    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param phase_guid: Optional: Filters time entries for given phases.
    :type phase_guid: List[str]
    :param time_entry_type_guid: Optional: Filters time entries for given time entry types.
    :type time_entry_type_guid: List[str]
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get time entries that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def time_entries_get_time_entries_for_user(request: web.Request, user_guid, start_date=None, end_date=None, phase_guid=None, time_entry_type_guid=None, first_row=None, row_count=None) -> web.Response:
    """Get all the time entries for a user.

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param start_date: Optional: starting date from which to get the time entries. Default all.
    :type start_date: str
    :param end_date: Optional: starting date to which to get the time entries. Default all.
    :type end_date: str
    :param phase_guid: Optional: Filters time entries for given phases.
    :type phase_guid: List[str]
    :param time_entry_type_guid: Optional: Filters time entries for given time entry types.
    :type time_entry_type_guid: List[str]
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def time_entries_get_time_entry(request: web.Request, guid) -> web.Response:
    """Get time entry by ID.

    

    :param guid: Id used to get the time entry.
    :type guid: str

    """
    return web.Response(status=200)


async def work_hours_get_deleted_work_hours(request: web.Request, page_token=None, row_count=None, project_guids=None, user_guids=None, deleted_since=None) -> web.Response:
    """Get the deleted work hours.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param project_guids: Optional: ID of the project for the deleted work hours to be fetched. If not provided, returns for all projects. Default all.
    :type project_guids: List[str]
    :param user_guids: Optional: ID of the user. If not provided, returns for all users. Default all.
    :type user_guids: List[str]
    :param deleted_since: Optional: Get work hours that have been deleted after this date time (greater or equal).
    :type deleted_since: str

    """
    deleted_since = util.deserialize_datetime(deleted_since)
    return web.Response(status=200)


async def work_hours_get_project_work_hours(request: web.Request, project_guid, is_billable=None, is_billed=None, start_date=None, end_date=None, page_token=None, row_count=None) -> web.Response:
    """Get all the work hours for phases of a project for invoicing

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param is_billable: Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param is_billed: Optional: Filter the work hours. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    :type is_billed: bool
    :param start_date: Optional: starting date from which to get the hours. Default all.
    :type start_date: str
    :param end_date: Optional: starting date to which to get the hours. Default all.
    :type end_date: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def work_hours_get_work_hour(request: web.Request, guid) -> web.Response:
    """Get work hour by ID

    

    :param guid: Id used to get the work hour.
    :type guid: str

    """
    return web.Response(status=200)


async def work_hours_get_work_hours(request: web.Request, page_token=None, row_count=None, changed_since=None, billable_status=None, event_date_start=None, event_date_end=None) -> web.Response:
    """Get the work hours.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get work hours that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param billable_status: Billable status type
    :type billable_status: dict | bytes
    :param event_date_start: Optional: Get work hours that have event date after this date time (greater or equal).
    :type event_date_start: str
    :param event_date_end: Optional: Get work hours that have event date before this date time (less or equal).
    :type event_date_end: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    billable_status = .from_dict(billable_status)
    event_date_start = util.deserialize_date(event_date_start)
    event_date_end = util.deserialize_date(event_date_end)
    return web.Response(status=200)


async def work_hours_get_work_hours_for_user(request: web.Request, user_guid, start_date=None, end_date=None, phase_guid=None, work_type_guid=None, page_token=None, row_count=None) -> web.Response:
    """Get all the work hours for a user

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param start_date: Optional: starting date from which to get the hours. Default all.
    :type start_date: str
    :param end_date: Optional: starting date to which to get the hours. Default all.
    :type end_date: str
    :param phase_guid: Optional: ID of the phase to get the hours for. Default all.
    :type phase_guid: List[str]
    :param work_type_guid: Optional: ID of the work type. Default all.
    :type work_type_guid: List[str]
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)
