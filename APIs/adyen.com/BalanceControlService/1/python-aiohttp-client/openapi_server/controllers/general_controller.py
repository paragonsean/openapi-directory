from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_transfer_request import BalanceTransferRequest
from openapi_server.models.balance_transfer_response import BalanceTransferResponse
from openapi_server import util


async def post_balance_transfer(request: web.Request, body=None) -> web.Response:
    """Start a balance transfer

    Starts a balance transfer request between merchant accounts. The following conditions must be met before you can successfully transfer balances:  * The source and destination merchant accounts must be under the same company account and legal entity.  * The source merchant account must have sufficient funds.  * The source and destination merchant accounts must have at least one common processing currency.  When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel. 

    :param body: 
    :type body: dict | bytes

    """
    body = BalanceTransferRequest.from_dict(body)
    return web.Response(status=200)
