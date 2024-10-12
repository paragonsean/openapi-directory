from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_account_positions_get200_response_inner import AccountsAccountPositionsGet200ResponseInner
from openapi_server.models.accounts_account_summary_get200_response import AccountsAccountSummaryGet200Response
from openapi_server.models.accounts_get200_response import AccountsGet200Response
from openapi_server import util


async def accounts_account_positions_get(request: web.Request, account) -> web.Response:
    """Account Positions

    Returns a list of positions for the indicated account. 

    :param account: Account Number
    :type account: str

    """
    return web.Response(status=200)


async def accounts_account_summary_get(request: web.Request, account) -> web.Response:
    """Account Values Summary

    Returns a list of account and margin balances associated with the account passed in the URL

    :param account: Account Number
    :type account: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, account) -> web.Response:
    """Brokerage Accounts

    Allows the caller to request a list of accounts associated with the session.

    :param account: Account Number
    :type account: str

    """
    return web.Response(status=200)
