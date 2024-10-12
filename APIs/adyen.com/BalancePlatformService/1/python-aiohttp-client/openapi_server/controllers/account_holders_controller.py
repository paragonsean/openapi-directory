from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_holder import AccountHolder
from openapi_server.models.account_holder_info import AccountHolderInfo
from openapi_server.models.paginated_balance_accounts_response import PaginatedBalanceAccountsResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_account_holders_id(request: web.Request, id) -> web.Response:
    """Get an account holder

    Returns an account holder.

    :param id: The unique identifier of the account holder.
    :type id: str

    """
    return web.Response(status=200)


async def get_account_holders_id_balance_accounts(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """Get all balance accounts of an account holder

    Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages, use the query parameters.   For example, to limit the page to 5 balance accounts and skip the first 10, use &#x60;/accountHolders/{id}/balanceAccounts?limit&#x3D;5&amp;offset&#x3D;10&#x60;.

    :param id: The unique identifier of the account holder.
    :type id: str
    :param offset: The number of items that you want to skip.
    :type offset: int
    :param limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page.
    :type limit: int

    """
    return web.Response(status=200)


async def patch_account_holders_id(request: web.Request, id, body=None) -> web.Response:
    """Update an account holder

    Updates an account holder. When updating an account holder resource, if a parameter is not provided in the request, it is left unchanged.

    :param id: The unique identifier of the account holder.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AccountHolder.from_dict(body)
    return web.Response(status=200)


async def post_account_holders(request: web.Request, body=None) -> web.Response:
    """Create an account holder

    Creates an account holder linked to a [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities).  

    :param body: 
    :type body: dict | bytes

    """
    body = AccountHolderInfo.from_dict(body)
    return web.Response(status=200)
