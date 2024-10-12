from typing import List, Dict
from aiohttp import web

from openapi_server.models.apps_permissions_resources_list_error_schema import AppsPermissionsResourcesListErrorSchema
from openapi_server.models.apps_permissions_resources_list_success_schema import AppsPermissionsResourcesListSuccessSchema
from openapi_server import util


async def apps_permissions_resources_list(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """apps_permissions_resources_list

    Returns list of resource grants this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str
    :param limit: The maximum number of items to return.
    :type limit: int

    """
    return web.Response(status=200)
