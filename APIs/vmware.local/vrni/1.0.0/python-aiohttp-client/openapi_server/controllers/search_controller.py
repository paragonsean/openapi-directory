from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.paged_list_response_with_time import PagedListResponseWithTime
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def search_entities(request: web.Request, body=None) -> web.Response:
    """Search entities

    Using search API you can search vRealize Network Insight entities by specifying entity type and filter expression. A filter expression is a predicate expression (similar to SQL where clause) used to define the search criteria. Please refer to API Guide on details of how to construct filter expression. A successful search request will return a list of entity ids that matches the search criteria.

    :param body: Search Request
    :type body: dict | bytes

    """
    body = SearchRequest.from_dict(body)
    return web.Response(status=200)
