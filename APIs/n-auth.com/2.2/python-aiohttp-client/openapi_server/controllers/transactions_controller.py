from typing import List, Dict
from aiohttp import web

from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_id import TransactionId
from openapi_server.models.transaction_result import TransactionResult
from openapi_server import util


async def create_transaction(request: web.Request, serverid, x_nonce, msg) -> web.Response:
    """Create a transaction to be approved within the current session.

    Create a transaction for approval within the current session. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param x_nonce: Nonce to identify the browser/webserver session
    :type x_nonce: str
    :param msg: 
    :type msg: dict | bytes

    """
    msg = Transaction.from_dict(msg)
    return web.Response(status=200)


async def get_transaction_result(request: web.Request, serverid, transactionid) -> web.Response:
    """Get transaction result for a given transaction.

    Get transaction result for a given transaction id. Required permission: &#39;sessions&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param transactionid: Base64 encoded transaction id
    :type transactionid: str

    """
    return web.Response(status=200)
