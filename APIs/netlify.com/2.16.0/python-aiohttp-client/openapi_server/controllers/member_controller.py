from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_add_member_setup import AccountAddMemberSetup
from openapi_server.models.account_update_member_setup import AccountUpdateMemberSetup
from openapi_server.models.error import Error
from openapi_server.models.member import Member
from openapi_server import util


async def add_member_to_account(request: web.Request, account_slug, account_add_member_setup) -> web.Response:
    """add_member_to_account

    

    :param account_slug: 
    :type account_slug: str
    :param account_add_member_setup: 
    :type account_add_member_setup: dict | bytes

    """
    account_add_member_setup = AccountAddMemberSetup.from_dict(account_add_member_setup)
    return web.Response(status=200)


async def get_account_member(request: web.Request, account_slug, member_id) -> web.Response:
    """get_account_member

    

    :param account_slug: 
    :type account_slug: str
    :param member_id: 
    :type member_id: str

    """
    return web.Response(status=200)


async def list_members_for_account(request: web.Request, account_slug) -> web.Response:
    """list_members_for_account

    

    :param account_slug: 
    :type account_slug: str

    """
    return web.Response(status=200)


async def remove_account_member(request: web.Request, account_slug, member_id) -> web.Response:
    """remove_account_member

    

    :param account_slug: 
    :type account_slug: str
    :param member_id: 
    :type member_id: str

    """
    return web.Response(status=200)


async def update_account_member(request: web.Request, account_slug, member_id, account_update_member_setup) -> web.Response:
    """update_account_member

    

    :param account_slug: 
    :type account_slug: str
    :param member_id: 
    :type member_id: str
    :param account_update_member_setup: 
    :type account_update_member_setup: dict | bytes

    """
    account_update_member_setup = AccountUpdateMemberSetup.from_dict(account_update_member_setup)
    return web.Response(status=200)
