from typing import List, Dict
from aiohttp import web

from openapi_server.models.close_account_request import CloseAccountRequest
from openapi_server.models.close_account_response import CloseAccountResponse
from openapi_server.models.create_account_request import CreateAccountRequest
from openapi_server.models.create_account_response import CreateAccountResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.update_account_response import UpdateAccountResponse
from openapi_server import util


async def post_close_account(request: web.Request, body=None) -> web.Response:
    """Close an account

    Closes an account. If an account is closed, you cannot process transactions, pay out its funds, or reopen it. If payments are made to a closed account, the payments are sent to your liable account.

    :param body: 
    :type body: dict | bytes

    """
    body = CloseAccountRequest.from_dict(body)
    return web.Response(status=200)


async def post_create_account(request: web.Request, body=None) -> web.Response:
    """Create an account

    Creates an account under an account holder. An account holder can have [multiple accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/account-holders-and-accounts#create-additional-accounts).

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccountRequest.from_dict(body)
    return web.Response(status=200)


async def post_update_account(request: web.Request, body=None) -> web.Response:
    """Update an account

    Updates the description or payout schedule of an account.

    :param body: 
    :type body: dict | bytes

    """
    body = UpdateAccountRequest.from_dict(body)
    return web.Response(status=200)
