from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_account import BalanceAccount
from openapi_server.models.balance_account_info import BalanceAccountInfo
from openapi_server.models.balance_account_update_request import BalanceAccountUpdateRequest
from openapi_server.models.paginated_payment_instruments_response import PaginatedPaymentInstrumentsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_balance_accounts_id(request: web.Request, id) -> web.Response:
    """Get a balance account

    Returns a balance account and its balances for the default currency and other currencies with a non-zero balance.

    :param id: The unique identifier of the balance account.
    :type id: str

    """
    return web.Response(status=200)


async def get_balance_accounts_id_payment_instruments(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """Get all payment instruments for a balance account

    Returns a paginated list of the payment instruments associated with a balance account.   To fetch multiple pages, use the query parameters.For example, to limit the page to 3 payment instruments and to skip the first 6, use &#x60;/balanceAccounts/{id}/paymentInstruments?limit&#x3D;3&amp;offset&#x3D;6&#x60;.

    :param id: The unique identifier of the balance account.
    :type id: str
    :param offset: The number of items that you want to skip.
    :type offset: int
    :param limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page.
    :type limit: int

    """
    return web.Response(status=200)


async def patch_balance_accounts_id(request: web.Request, id, body=None) -> web.Response:
    """Update a balance account

    Updates a balance account.

    :param id: The unique identifier of the balance account.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = BalanceAccountUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def post_balance_accounts(request: web.Request, body=None) -> web.Response:
    """Create a balance account

    Creates a balance account that holds the funds of the associated account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = BalanceAccountInfo.from_dict(body)
    return web.Response(status=200)
