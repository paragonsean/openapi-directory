from typing import List, Dict
from aiohttp import web

from openapi_server.models.sso_strategy_entity import SsoStrategyEntity
from openapi_server import util


async def get_sso_strategies(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List Sso Strategies

    List Sso Strategies

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_sso_strategies_id(request: web.Request, id) -> web.Response:
    """Show Sso Strategy

    Show Sso Strategy

    :param id: Sso Strategy ID.
    :type id: int

    """
    return web.Response(status=200)


async def post_sso_strategies_id_sync(request: web.Request, id) -> web.Response:
    """Synchronize provisioning data with the SSO remote server.

    Synchronize provisioning data with the SSO remote server.

    :param id: Sso Strategy ID.
    :type id: int

    """
    return web.Response(status=200)
