from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_account_trades_get200_response_inner import AccountsAccountTradesGet200ResponseInner
from openapi_server import util


async def accounts_account_trades_get(request: web.Request, account, body=None) -> web.Response:
    """Returns trades in account

    Returns a list of trades for the account starting at the given &#39;since&#39; date to the current time (now()). Timezone is UTC. Any request with a future since date or going further than one week will result in an HTTP 400 bad request response. Calling /trades without since will return all trades for the past 24 hours. 

    :param account: Account Number
    :type account: str
    :param body: Start time specified in UTC. Allowed formats are \&quot;yyyy-MM-dd\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;. Time is optional and is set to midnight if omitted, e.g. \&quot;00:00:00 hh:mm:ss\&quot;. 
    :type body: str

    """
    return web.Response(status=200)
