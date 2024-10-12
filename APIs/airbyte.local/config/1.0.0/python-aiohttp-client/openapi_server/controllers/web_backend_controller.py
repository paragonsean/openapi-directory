from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.connection_state_type import ConnectionStateType
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.web_backend_check_updates_read import WebBackendCheckUpdatesRead
from openapi_server.models.web_backend_connection_create import WebBackendConnectionCreate
from openapi_server.models.web_backend_connection_list_request_body import WebBackendConnectionListRequestBody
from openapi_server.models.web_backend_connection_read import WebBackendConnectionRead
from openapi_server.models.web_backend_connection_read_list import WebBackendConnectionReadList
from openapi_server.models.web_backend_connection_request_body import WebBackendConnectionRequestBody
from openapi_server.models.web_backend_connection_update import WebBackendConnectionUpdate
from openapi_server.models.web_backend_geographies_list_result import WebBackendGeographiesListResult
from openapi_server.models.web_backend_workspace_state import WebBackendWorkspaceState
from openapi_server.models.web_backend_workspace_state_result import WebBackendWorkspaceStateResult
from openapi_server import util


async def get_state_type(request: web.Request, body) -> web.Response:
    """Fetch the current state type for a connection.

    

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def web_backend_check_updates(request: web.Request, ) -> web.Response:
    """Returns a summary of source and destination definitions that could be updated.

    


    """
    return web.Response(status=200)


async def web_backend_create_connection(request: web.Request, body) -> web.Response:
    """Create a connection

    

    :param body: 
    :type body: dict | bytes

    """
    body = WebBackendConnectionCreate.from_dict(body)
    return web.Response(status=200)


async def web_backend_get_connection(request: web.Request, body) -> web.Response:
    """Get a connection

    

    :param body: 
    :type body: dict | bytes

    """
    body = WebBackendConnectionRequestBody.from_dict(body)
    return web.Response(status=200)


async def web_backend_get_workspace_state(request: web.Request, body=None) -> web.Response:
    """Returns the current state of a workspace

    

    :param body: 
    :type body: dict | bytes

    """
    body = WebBackendWorkspaceState.from_dict(body)
    return web.Response(status=200)


async def web_backend_list_connections_for_workspace(request: web.Request, body) -> web.Response:
    """Returns all non-deleted connections for a workspace.

    

    :param body: 
    :type body: dict | bytes

    """
    body = WebBackendConnectionListRequestBody.from_dict(body)
    return web.Response(status=200)


async def web_backend_list_geographies(request: web.Request, ) -> web.Response:
    """Returns available geographies can be selected to run data syncs in a particular geography. The &#39;auto&#39; entry indicates that the sync will be automatically assigned to a geography according to the platform default behavior. Entries other than &#39;auto&#39; are two-letter country codes that follow the ISO 3166-1 alpha-2 standard. 

    Returns all available geographies in which a data sync can run.


    """
    return web.Response(status=200)


async def web_backend_update_connection(request: web.Request, body) -> web.Response:
    """Update a connection

    Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Any operations that lack an ID will be created. Then, the newly created operationId will be applied to the connection along with the rest of the operationIds in the request body. Apply a patch-style update to a connection. Only fields present on the update request body will be updated. Note that if a catalog is present in the request body, the connection&#39;s entire catalog will be replaced with the catalog from the request. This means that to modify a single stream, the entire new catalog containing the updated stream needs to be sent. 

    :param body: 
    :type body: dict | bytes

    """
    body = WebBackendConnectionUpdate.from_dict(body)
    return web.Response(status=200)
