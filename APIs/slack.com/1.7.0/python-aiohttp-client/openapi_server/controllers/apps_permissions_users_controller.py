from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def apps_permissions_users_list(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """apps_permissions_users_list

    Returns list of user grants and corresponding scopes this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str
    :param limit: The maximum number of items to return.
    :type limit: int

    """
    return web.Response(status=200)


async def apps_permissions_users_request(request: web.Request, token, scopes, trigger_id, user) -> web.Response:
    """apps_permissions_users_request

    Enables an app to trigger a permissions modal to grant an app access to a user access scope.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param scopes: A comma separated list of user scopes to request for
    :type scopes: str
    :param trigger_id: Token used to trigger the request
    :type trigger_id: str
    :param user: The user this scope is being requested for
    :type user: str

    """
    return web.Response(status=200)
