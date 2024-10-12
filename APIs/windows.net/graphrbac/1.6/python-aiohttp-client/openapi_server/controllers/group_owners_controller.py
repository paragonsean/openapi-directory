from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError
from openapi_server import util


async def groups_list_owners(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """Directory objects that are owners of the group.

    The owners are a set of non-admin users who are allowed to modify this object.

    :param object_id: The object ID of the group for which to get owners.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
