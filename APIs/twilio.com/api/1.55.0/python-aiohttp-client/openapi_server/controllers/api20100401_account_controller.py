from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_enum_status import AccountEnumStatus
from openapi_server.models.api_v2010_account import ApiV2010Account
from openapi_server.models.list_account_response import ListAccountResponse
from openapi_server import util


async def create_account(request: web.Request, friendly_name=None) -> web.Response:
    """create_account

    Create a new Twilio Subaccount from the account making the request

    :param friendly_name: A human readable description of the account to create, defaults to &#x60;SubAccount Created at {YYYY-MM-DD HH:MM meridian}&#x60;
    :type friendly_name: str

    """
    return web.Response(status=200)


async def fetch_account(request: web.Request, sid) -> web.Response:
    """fetch_account

    Fetch the account specified by the provided Account Sid

    :param sid: The Account Sid that uniquely identifies the account to fetch
    :type sid: str

    """
    return web.Response(status=200)


async def list_account(request: web.Request, friendly_name=None, status=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_account

    Retrieves a collection of Accounts belonging to the account used to make the request

    :param friendly_name: Only return the Account resources with friendly names that exactly match this name.
    :type friendly_name: str
    :param status: Only return Account resources with the given status. Can be &#x60;closed&#x60;, &#x60;suspended&#x60; or &#x60;active&#x60;.
    :type status: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_account(request: web.Request, sid, friendly_name=None, status=None) -> web.Response:
    """update_account

    Modify the properties of a given Account

    :param sid: The Account Sid that uniquely identifies the account to update
    :type sid: str
    :param friendly_name: Update the human-readable description of this Account
    :type friendly_name: str
    :param status: 
    :type status: str

    """
    return web.Response(status=200)
