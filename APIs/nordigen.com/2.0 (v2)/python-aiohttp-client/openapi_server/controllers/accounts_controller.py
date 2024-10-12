from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server import util


async def retrieve_account_balances_v2(request: web.Request, id) -> web.Response:
    """retrieve_account_balances_v2

    Access account balances.  Balances will be returned in Berlin Group PSD2 format.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def retrieve_account_details_v2(request: web.Request, id) -> web.Response:
    """retrieve_account_details_v2

    Access account details.  Account details will be returned in Berlin Group PSD2 format.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def retrieve_account_metadata(request: web.Request, id) -> web.Response:
    """retrieve_account_metadata

    Access account metadata.  Information about the account record, such as the processing status and IBAN.  Account status is recalculated based on the error count in the latest req.

    :param id: 
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def retrieve_account_transactions_v22(request: web.Request, id, date_from=None, date_to=None) -> web.Response:
    """retrieve_account_transactions_v22

    Access account transactions.  Transactions will be returned in Berlin Group PSD2 format.

    :param id: 
    :type id: str
    :type id: str
    :param date_from: 
    :type date_from: str
    :param date_to: 
    :type date_to: str

    """
    date_from = util.deserialize_date(date_from)
    date_to = util.deserialize_date(date_to)
    return web.Response(status=200)
