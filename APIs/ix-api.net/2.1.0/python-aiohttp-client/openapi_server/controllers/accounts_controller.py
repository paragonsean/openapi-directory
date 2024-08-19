from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_request import AccountRequest
from openapi_server.models.account_update import AccountUpdate
from openapi_server.models.account_update_partial import AccountUpdatePartial
from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server import util


async def accounts_create(request: web.Request, body=None) -> web.Response:
    """accounts_create

    Create a new account.

    :param body: Account Request
    :type body: dict | bytes

    """
    body = AccountRequest.from_dict(body)
    return web.Response(status=200)


async def accounts_destroy(request: web.Request, id) -> web.Response:
    """accounts_destroy

    Accounts can be deleted, when all services and configs are decommissioned or the account is not longer referenced e.g. as a &#x60;managing_account&#x60; or &#x60;billing_account&#x60;.  Deleting an account will cascade to &#x60;contacts&#x60; and &#x60;role-assignments&#x60;.  The request will immediately fail, if the above preconditions are not met.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def accounts_list(request: web.Request, id=None, state=None, state__is_not=None, managing_account=None, billable=None, external_ref=None, name=None) -> web.Response:
    """accounts_list

    Retrieve a list of &#x60;Account&#x60;s.  This includes all accounts the currently authorized account is managing and the current account itself.

    :param id: Filter by id
    :type id: List[str]
    :param state: Filter by state
    :type state: str
    :param state__is_not: Filter by state__is_not
    :type state__is_not: str
    :param managing_account: Filter by managing_account
    :type managing_account: str
    :param billable: Filter by billable
    :type billable: int
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param name: Filter by name
    :type name: str

    """
    return web.Response(status=200)


async def accounts_partial_update(request: web.Request, id, body=None) -> web.Response:
    """accounts_partial_update

    Update parts of an account.

    :param id: Get by id
    :type id: str
    :param body: Account Update Request
    :type body: dict | bytes

    """
    body = AccountUpdatePartial.from_dict(body)
    return web.Response(status=200)


async def accounts_read(request: web.Request, id) -> web.Response:
    """accounts_read

    Get a single account.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, id, body=None) -> web.Response:
    """accounts_update

    Update the entire account.

    :param id: Get by id
    :type id: str
    :param body: Account Update Request
    :type body: dict | bytes

    """
    body = AccountUpdate.from_dict(body)
    return web.Response(status=200)
