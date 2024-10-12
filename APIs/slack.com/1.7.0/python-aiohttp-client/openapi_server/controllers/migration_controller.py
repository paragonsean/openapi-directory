from typing import List, Dict
from aiohttp import web

from openapi_server.models.migration_exchange_error_schema import MigrationExchangeErrorSchema
from openapi_server.models.migration_exchange_success_schema import MigrationExchangeSuccessSchema
from openapi_server import util


async def migration_exchange(request: web.Request, token, users, team_id=None, to_old=None) -> web.Response:
    """migration_exchange

    For Enterprise Grid workspaces, map local user IDs to global user IDs

    :param token: Authentication token. Requires scope: &#x60;tokens.basic&#x60;
    :type token: str
    :param users: A comma-separated list of user ids, up to 400 per request
    :type users: str
    :param team_id: Specify team_id starts with &#x60;T&#x60; in case of Org Token
    :type team_id: str
    :param to_old: Specify &#x60;true&#x60; to convert &#x60;W&#x60; global user IDs to workspace-specific &#x60;U&#x60; IDs. Defaults to &#x60;false&#x60;.
    :type to_old: bool

    """
    return web.Response(status=200)
