from typing import List, Dict
from aiohttp import web

from openapi_server.models.statement_response import StatementResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def get_statements(request: web.Request, account_id=None, container=None, from_date=None, is_latest=None, status=None) -> web.Response:
    """Get Statements

    The statements service is used to get the list of statement related information. &lt;br&gt;By default, all the latest statements of active and to be closed accounts are retrieved for the user. &lt;br&gt;Certain sites do not have both a statement date and a due date. When a fromDate is passed as an input, all the statements that have the due date on or after the passed date are retrieved. &lt;br&gt;For sites that do not have the due date, statements that have the statement date on or after the passed date are retrieved. &lt;br&gt;The default value of \&quot;isLatest\&quot; is true. To retrieve historical statements isLatest needs to be set to false.&lt;br&gt;

    :param account_id: accountId
    :type account_id: str
    :param container: creditCard/loan/insurance
    :type container: str
    :param from_date: from date for statement retrieval (YYYY-MM-DD)
    :type from_date: str
    :param is_latest: isLatest (true/false)
    :type is_latest: str
    :param status: ACTIVE,TO_BE_CLOSED,CLOSED
    :type status: str

    """
    return web.Response(status=200)
