from typing import List, Dict
from aiohttp import web

from openapi_server.models.fixed_amount_list import FixedAmountList
from openapi_server import util


async def fixed_amount_get(request: web.Request, updated_after=None, entry_date_from=None, entry_date_to=None, project_id=None, task_id=None, is_invoiced=None, page_size=None, page_number=None, sort=None) -> web.Response:
    """Gets list of Fixed Amounts

    

    :param updated_after: 
    :type updated_after: str
    :param entry_date_from: 
    :type entry_date_from: str
    :param entry_date_to: 
    :type entry_date_to: str
    :param project_id: (Optional) The ProjectID of a Project to filter Fixed Amounts for
    :type project_id: int
    :param task_id: (Optional) The TaskID of a Task to filter Fixed Amounts for
    :type task_id: int
    :param is_invoiced: 
    :type is_invoiced: bool
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot;
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    entry_date_from = util.deserialize_datetime(entry_date_from)
    entry_date_to = util.deserialize_datetime(entry_date_to)
    return web.Response(status=200)
