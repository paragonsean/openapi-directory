from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_type_enum import AccountTypeEnum
from openapi_server.models.get_account_response import GetAccountResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.ownership_type_enum import OwnershipTypeEnum
from openapi_server import util


async def accounts_get(request: web.Request, page_size=None, filter_account_type=None, filter_ownership_type=None) -> web.Response:
    """List accounts

    Retrieve a paginated list of all accounts for the currently authenticated user. The returned list is paginated and can be scrolled by following the &#x60;prev&#x60; and &#x60;next&#x60; links where present. 

    :param page_size: The number of records to return in each page. 
    :type page_size: int
    :param filter_account_type: The type of account for which to return records. This can be used to filter Savers from spending accounts. 
    :type filter_account_type: dict | bytes
    :param filter_ownership_type: The account ownership structure for which to return records. This can be used to filter 2Up accounts from Up accounts. 
    :type filter_ownership_type: dict | bytes

    """
    filter_account_type = .from_dict(filter_account_type)
    filter_ownership_type = .from_dict(filter_ownership_type)
    return web.Response(status=200)


async def accounts_id_get(request: web.Request, id) -> web.Response:
    """Retrieve account

    Retrieve a specific account by providing its unique identifier. 

    :param id: The unique identifier for the account. 
    :type id: str

    """
    return web.Response(status=200)
