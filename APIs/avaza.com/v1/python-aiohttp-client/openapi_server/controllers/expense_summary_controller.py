from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_summary_result import ExpenseSummaryResult
from openapi_server import util


async def expense_summary_get(request: web.Request, model_group_by=None, model_expense_date_from=None, model_expense_date_to=None, model_user_id=None, model_project_id=None) -> web.Response:
    """Gets Basic Summary of Expense Statistics

    

    :param model_group_by: (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \&quot;Category\&quot;, \&quot;ChargeableStatus\&quot;, \&quot;Merchant\&quot;, \&quot;ApprovalStatus\&quot;, \&quot;ReimbursementStatus\&quot;, \&quot;Customer\&quot;, \&quot;Project\&quot;, \&quot;User\&quot;, \&quot;Task\&quot;, \&quot;Year\&quot;, \&quot;Month\&quot;, \&quot;Day\&quot;, \&quot;Week\&quot;.
    :type model_group_by: List[str]
    :param model_expense_date_from: (Required) Filter for expenses with expense dates greater or equal to the specified date. e.g. 2019-01-25.
    :type model_expense_date_from: str
    :param model_expense_date_to: (Required) Filter for expenses with an expense date smaller or equal to the specified  date. e.g. 2019-01-25.
    :type model_expense_date_to: str
    :param model_user_id: (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose expenses should be retrieved. If the current user doesn&#39;t have impersonation rights, then they will only see their own data.
    :type model_user_id: List[int]
    :param model_project_id: (Optional) Filter by Project
    :type model_project_id: int

    """
    model_expense_date_from = util.deserialize_datetime(model_expense_date_from)
    model_expense_date_to = util.deserialize_datetime(model_expense_date_to)
    return web.Response(status=200)
