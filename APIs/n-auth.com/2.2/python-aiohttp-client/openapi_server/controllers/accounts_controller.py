from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server import util


async def delete_account(request: web.Request, serverid, accountid) -> web.Response:
    """Delete specific account

    Delete an account. Required permission: &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param accountid: Account id
    :type accountid: int

    """
    return web.Response(status=200)


async def delete_user_accounts_0(request: web.Request, serverid, userid) -> web.Response:
    """Delete all accounts of a specific user

    Delete all accounts corresponding to this user. The user itself is not deleted. Required permission: &#39;accounts&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)


async def get_account(request: web.Request, serverid, accountid) -> web.Response:
    """Get specific account

    Returns the account. Required permission: &#39;sessions&#39; or &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param accountid: Account id
    :type accountid: int

    """
    return web.Response(status=200)


async def get_all_accounts(request: web.Request, serverid, filter=None, limit=None, marker=None, sort=None) -> web.Response:
    """Get all accounts

    Returns all account. Required permission &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param filter: Filter users based on an attribute. Takes the format *attributename&#x3D;attributevalue*. You can filter for multiple values at once, e.g. *group&#x3D;in:group1,group2*
    :type filter: str
    :param limit: Limit the number of results
    :type limit: int
    :param marker: Offset in the result list
    :type marker: int
    :param sort: Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    :type sort: str

    """
    return web.Response(status=200)


async def get_user_0(request: web.Request, serverid, userid, limit=None, marker=None, sort=None) -> web.Response:
    """Get all accounts of a specific user

    Returns an array containing all accounts corresponding to this user. Required permission: &#39;sessions&#39; or &#39;users&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param userid: User name
    :type userid: str
    :param limit: Limit the number of results
    :type limit: int
    :param marker: Offset in the result list
    :type marker: int
    :param sort: Sort the results by column. You can also specify ascending (default if not specified) or descending, e.g., *column:asc* . You can also sort by multiple columns, e.g., *column1:desc,column2:asc*
    :type sort: str

    """
    return web.Response(status=200)


async def update_account(request: web.Request, serverid, accountid, blocked) -> web.Response:
    """Update specific account

    Update an account. The only available change is (un)blocking the account. Required permission: &#39;accounts&#39;. 

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param accountid: Account id
    :type accountid: int
    :param blocked: True if the account is blocked
    :type blocked: bool

    """
    return web.Response(status=200)


async def update_account_user(request: web.Request, serverid, accountid, userid) -> web.Response:
    """Update user of the given account.

    Update the user of the given account. Required permission: &#39;accounts&#39;.

    :param serverid: Base64 encoded server id
    :type serverid: str
    :param accountid: Account id
    :type accountid: int
    :param userid: User name
    :type userid: str

    """
    return web.Response(status=200)
