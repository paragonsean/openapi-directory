from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_permissions_scopes_list_success_schema import ApiPermissionsScopesListSuccessSchema
from openapi_server.models.apps_permissions_info_error_schema import AppsPermissionsInfoErrorSchema
from openapi_server.models.apps_permissions_info_schema import AppsPermissionsInfoSchema
from openapi_server.models.apps_permissions_request_error_schema import AppsPermissionsRequestErrorSchema
from openapi_server.models.apps_permissions_request_schema import AppsPermissionsRequestSchema
from openapi_server.models.apps_permissions_resources_list_error_schema import AppsPermissionsResourcesListErrorSchema
from openapi_server.models.apps_permissions_resources_list_success_schema import AppsPermissionsResourcesListSuccessSchema
from openapi_server.models.apps_permissions_scopes_list_error_schema import AppsPermissionsScopesListErrorSchema
from openapi_server.models.apps_uninstall_error_schema import AppsUninstallErrorSchema
from openapi_server.models.apps_uninstall_schema import AppsUninstallSchema
from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def apps_event_authorizations_list_0(request: web.Request, token, event_context, cursor=None, limit=None) -> web.Response:
    """apps_event_authorizations_list_0

    Get a list of authorizations for the given event context. Each authorization represents an app installation that the event is visible to.

    :param token: Authentication token. Requires scope: &#x60;authorizations:read&#x60;
    :type token: str
    :param event_context: 
    :type event_context: str
    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def apps_permissions_info_0(request: web.Request, token=None) -> web.Response:
    """apps_permissions_info_0

    Returns list of permissions this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def apps_permissions_request_0(request: web.Request, token, scopes, trigger_id) -> web.Response:
    """apps_permissions_request_0

    Allows an app to request additional scopes

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param scopes: A comma separated list of scopes to request for
    :type scopes: str
    :param trigger_id: Token used to trigger the permissions API
    :type trigger_id: str

    """
    return web.Response(status=200)


async def apps_permissions_resources_list_0(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """apps_permissions_resources_list_0

    Returns list of resource grants this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str
    :param limit: The maximum number of items to return.
    :type limit: int

    """
    return web.Response(status=200)


async def apps_permissions_scopes_list_0(request: web.Request, token) -> web.Response:
    """apps_permissions_scopes_list_0

    Returns list of scopes this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str

    """
    return web.Response(status=200)


async def apps_permissions_users_list_0(request: web.Request, token, cursor=None, limit=None) -> web.Response:
    """apps_permissions_users_list_0

    Returns list of user grants and corresponding scopes this app has on a team.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param cursor: Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail.
    :type cursor: str
    :param limit: The maximum number of items to return.
    :type limit: int

    """
    return web.Response(status=200)


async def apps_permissions_users_request_0(request: web.Request, token, scopes, trigger_id, user) -> web.Response:
    """apps_permissions_users_request_0

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


async def apps_uninstall(request: web.Request, token=None, client_id=None, client_secret=None) -> web.Response:
    """apps_uninstall

    Uninstalls your app from a workspace.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param client_id: Issued when you created your application.
    :type client_id: str
    :param client_secret: Issued when you created your application.
    :type client_secret: str

    """
    return web.Response(status=200)
