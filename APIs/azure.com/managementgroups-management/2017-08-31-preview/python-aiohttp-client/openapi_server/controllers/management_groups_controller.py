from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group_list_result import ManagementGroupListResult
from openapi_server.models.management_group_with_hierarchy import ManagementGroupWithHierarchy
from openapi_server import util


async def management_groups_get(request: web.Request, group_id, api_version, expand=None, recurse=None) -> web.Response:
    """management_groups_get

    Get the details of the management group. 

    :param group_id: Management Group ID.
    :type group_id: str
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-08-31-preview.
    :type api_version: str
    :param expand: The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload.
    :type expand: str
    :param recurse: The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload.
    :type recurse: bool

    """
    return web.Response(status=200)


async def management_groups_list(request: web.Request, api_version, skiptoken=None) -> web.Response:
    """management_groups_list

    List management groups for the authenticated user. 

    :param api_version: Version of the API to be used with the client request. The current version is 2017-08-31-preview.
    :type api_version: str
    :param skiptoken: Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    :type skiptoken: str

    """
    return web.Response(status=200)
