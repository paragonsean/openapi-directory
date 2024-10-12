from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.get_objects_parameters import GetObjectsParameters
from openapi_server import util


async def objects_get_objects_by_object_ids(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """objects_get_objects_by_object_ids

    Gets the directory objects specified in a list of object IDs. You can also specify which resource collections (users, groups, etc.) should be searched by specifying the optional types parameter.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Objects filtering parameters.
    :type body: dict | bytes

    """
    body = GetObjectsParameters.from_dict(body)
    return web.Response(status=200)
