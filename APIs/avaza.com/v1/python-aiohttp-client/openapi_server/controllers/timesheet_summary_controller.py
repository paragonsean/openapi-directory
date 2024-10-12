from typing import List, Dict
from aiohttp import web

from openapi_server.models.timesheet_summary_result import TimesheetSummaryResult
from openapi_server import util


async def timesheet_summary_get(request: web.Request, model_group_by=None, model_entry_date_from=None, model_entry_date_to=None, model_user_id=None, model_project_id=None, model_is_billable=None, model_is_invoiced=None) -> web.Response:
    """Gets Basic Summary of Timesheet Statistics

    

    :param model_group_by: (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;Category\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;.
    :type model_group_by: List[str]
    :param model_entry_date_from: (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
    :type model_entry_date_from: str
    :param model_entry_date_to: (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00
    :type model_entry_date_to: str
    :param model_user_id: (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data.
    :type model_user_id: List[int]
    :param model_project_id: (Optional) Filter by Project
    :type model_project_id: int
    :param model_is_billable: (Optional) Filter by the billable status of Timesheets.
    :type model_is_billable: bool
    :param model_is_invoiced: (Optional) Filter for timesheets by whether they have been Invoiced or not.
    :type model_is_invoiced: bool

    """
    model_entry_date_from = util.deserialize_datetime(model_entry_date_from)
    model_entry_date_to = util.deserialize_datetime(model_entry_date_to)
    return web.Response(status=200)
