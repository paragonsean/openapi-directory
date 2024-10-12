from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_membership import AccountMembership
from openapi_server.models.account_setup import AccountSetup
from openapi_server.models.account_update_setup import AccountUpdateSetup
from openapi_server.models.error import Error
from openapi_server import util


async def cancel_account(request: web.Request, account_id) -> web.Response:
    """cancel_account

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def create_account(request: web.Request, account_setup) -> web.Response:
    """create_account

    

    :param account_setup: 
    :type account_setup: dict | bytes

    """
    account_setup = AccountSetup.from_dict(account_setup)
    return web.Response(status=200)


async def get_account(request: web.Request, account_id) -> web.Response:
    """get_account

    

    :param account_id: 
    :type account_id: str

    """
    return web.Response(status=200)


async def list_accounts_for_user(request: web.Request, ) -> web.Response:
    """list_accounts_for_user

    


    """
    return web.Response(status=200)


async def update_account(request: web.Request, account_id, account_update_setup=None) -> web.Response:
    """update_account

    

    :param account_id: 
    :type account_id: str
    :param account_update_setup: 
    :type account_update_setup: dict | bytes

    """
    account_update_setup = AccountUpdateSetup.from_dict(account_update_setup)
    return web.Response(status=200)
