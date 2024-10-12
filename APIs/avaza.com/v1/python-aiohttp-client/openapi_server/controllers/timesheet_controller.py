from typing import List, Dict
from aiohttp import web

from openapi_server.models.new_timesheet import NewTimesheet
from openapi_server.models.timesheet_details import TimesheetDetails
from openapi_server.models.timesheet_list import TimesheetList
from openapi_server.models.update_timesheet_model import UpdateTimesheetModel
from openapi_server import util


async def timesheet_delete(request: web.Request, id) -> web.Response:
    """Delete a Timesheet Entry

    

    :param id: The id of the timesheet entry to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def timesheet_get(request: web.Request, updated_after=None, entry_date_from=None, entry_date_to=None, user_id=None, user_email=None, category_name=None, project_id=None, is_billable=None, is_invoiced=None, is_timer_running=None, page_size=None, page_number=None, include_invoice_details=None, sort=None) -> web.Response:
    """Gets list of Timsheets

    

    :param updated_after: 
    :type updated_after: str
    :param entry_date_from: 
    :type entry_date_from: str
    :param entry_date_to: 
    :type entry_date_to: str
    :param user_id: The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users.
    :type user_id: int
    :param user_email: 
    :type user_email: str
    :param category_name: 
    :type category_name: str
    :param project_id: 
    :type project_id: int
    :param is_billable: 
    :type is_billable: bool
    :param is_invoiced: 
    :type is_invoiced: bool
    :param is_timer_running: 
    :type is_timer_running: bool
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param include_invoice_details: Defaults to false. When true, the InvoiceIDFK value will be included in the response.
    :type include_invoice_details: bool
    :param sort: Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot;
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    entry_date_from = util.deserialize_datetime(entry_date_from)
    entry_date_to = util.deserialize_datetime(entry_date_to)
    return web.Response(status=200)


async def timesheet_get_by_id(request: web.Request, id) -> web.Response:
    """Gets a Timesheet Entry by Timesheet ID

    

    :param id: Timesheet ID number
    :type id: int

    """
    return web.Response(status=200)


async def timesheet_post(request: web.Request, model) -> web.Response:
    """Create a new Timesheet Entry

    

    :param model: 
    :type model: dict | bytes

    """
    model = NewTimesheet.from_dict(model)
    return web.Response(status=200)


async def timesheet_put(request: web.Request, model) -> web.Response:
    """Update a Timesheet

    The FieldsToUpdate field expects a string array collection of the field names you would like updated. Valid fields to update inlcude \&quot;ProjectIDFK\&quot;, \&quot;TimeSheetCategoryIDFK\&quot;, \&quot;TaskIDFK\&quot;, \&quot;Duration\&quot;, \&quot;EntryDate\&quot;, \&quot;Notes\&quot;, \&quot;hasStartEndTime\&quot;, \&quot;CustomMetadata\&quot;. If you intend to provide start/end times on timesheets, this is achieved by including the start time in the EntryDate field (Iso date format), along with a Duration (decimal format).

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateTimesheetModel.from_dict(model)
    return web.Response(status=200)
