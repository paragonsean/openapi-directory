from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError
from openapi_server.models.user import User
from openapi_server import util


async def signed_in_user_get(request: web.Request, api_version, tenant_id) -> web.Response:
    """signed_in_user_get

    Gets the details for the currently logged-in user.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def signed_in_user_list_owned_objects(request: web.Request, api_version, tenant_id) -> web.Response:
    """signed_in_user_list_owned_objects

    Get the list of directory objects that are owned by the user.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
