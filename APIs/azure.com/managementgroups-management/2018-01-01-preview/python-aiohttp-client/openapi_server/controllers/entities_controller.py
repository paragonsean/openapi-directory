from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_list_result import EntityListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def entities_list(request: web.Request, api_version, skiptoken=None, group_name=None, cache_control=None) -> web.Response:
    """entities_list

    List all entities (Management Groups, Subscriptions, etc.) for the authenticated user. 

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str
    :param skiptoken: Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    :type skiptoken: str
    :param group_name: A filter which allows the call to be filtered for a specific group.
    :type group_name: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)
