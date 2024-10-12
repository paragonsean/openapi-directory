from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server.models.new_account import NewAccount
from openapi_server import util


async def add_account(request: web.Request, body) -> web.Response:
    """Add a new account

    Creates a new fire.com account.  **Please note there is a charge associated with creating a new account.** 

    :param body: Details of the new account
    :type body: dict | bytes

    """
    body = NewAccount.from_dict(body)
    return web.Response(status=200)


async def get_account_by_id(request: web.Request, ican) -> web.Response:
    """Retrieve the details of a fire.com Account

    You can retrieve the details of a fire.com Account by its &#x60;ican&#x60;.

    :param ican: 
    :type ican: int

    """
    return web.Response(status=200)


async def get_accounts(request: web.Request, ) -> web.Response:
    """List all fire.com Accounts

    Returns all your fire.com Accounts. Ordered by Alias ascending. Can be paginated.


    """
    return web.Response(status=200)
