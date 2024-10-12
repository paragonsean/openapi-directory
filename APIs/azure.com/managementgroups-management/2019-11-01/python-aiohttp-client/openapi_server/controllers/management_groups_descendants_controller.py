from typing import List, Dict
from aiohttp import web

from openapi_server.models.descendant_list_result import DescendantListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def management_groups_get_descendants(request: web.Request, group_id, api_version, skiptoken=None, top=None) -> web.Response:
    """management_groups_get_descendants

    List all entities that descend from a management group.

    :param group_id: Management Group ID.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str
    :param skiptoken: Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param top: Number of elements to return when retrieving results. Passing this in will override $skipToken.
    :type top: int

    """
    return web.Response(status=200)
