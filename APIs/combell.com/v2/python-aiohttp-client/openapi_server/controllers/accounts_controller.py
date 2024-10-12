from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_detail import AccountDetail
from openapi_server.models.asset_type import AssetType
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_account import CreateAccount
from openapi_server import util


async def create_account(request: web.Request, body=None) -> web.Response:
    """Create a new account

    The creation of an account requires some background processing. There is no instant feedback of the creation status.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateAccount.from_dict(body)
    return web.Response(status=200)


async def get_account(request: web.Request, account_id, account_id2) -> web.Response:
    """Get a specific account

    

    :param account_id: The id of the account.
    :type account_id: int
    :param account_id2: Automatically added
    :type account_id2: str

    """
    return web.Response(status=200)


async def get_accounts(request: web.Request, skip=None, take=None, asset_type=None, identifier=None) -> web.Response:
    """Overview of accounts

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int
    :param asset_type: Filters the list, returning only accounts containing the specified asset type.
    :type asset_type: dict | bytes
    :param identifier: Return only accounts, matching the specified identifier.
    :type identifier: str

    """
    asset_type = .from_dict(asset_type)
    return web.Response(status=200)
