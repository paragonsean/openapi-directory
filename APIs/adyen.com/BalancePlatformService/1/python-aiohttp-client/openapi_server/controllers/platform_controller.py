from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform import BalancePlatform
from openapi_server.models.paginated_account_holders_response import PaginatedAccountHoldersResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_balance_platforms_id(request: web.Request, id) -> web.Response:
    """Get a balance platform

    Returns a balance platform.

    :param id: The unique identifier of the balance platform.
    :type id: str

    """
    return web.Response(status=200)


async def get_balance_platforms_id_account_holders(request: web.Request, id, offset=None, limit=None) -> web.Response:
    """Get all account holders under a balance platform

    Returns a paginated list of all the account holders that belong to the balance platform. To fetch multiple pages, use the query parameters.   For example, to limit the page to 5 account holders and to skip the first 20, use &#x60;/balancePlatforms/{id}/accountHolders?limit&#x3D;5&amp;offset&#x3D;20&#x60;.

    :param id: The unique identifier of the balance platform.
    :type id: str
    :param offset: The number of items that you want to skip.
    :type offset: int
    :param limit: The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page.
    :type limit: int

    """
    return web.Response(status=200)
