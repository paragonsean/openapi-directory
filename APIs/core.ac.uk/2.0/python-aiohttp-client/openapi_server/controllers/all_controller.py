from typing import List, Dict
from aiohttp import web

from openapi_server.models.search_all_response import SearchAllResponse
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def search_post(request: web.Request, body) -> web.Response:
    """Batch operation for search through all resources

    Method accepts a JSON array of search queries. It searches through all resources and returns a JSON array with search results for each of the queries. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. Furthermore, the responses are oredered based on the order of the request items. The metadata of each resource need to be obtained through an appropriate method.

    :param body: JSON array with search queries and pagination parameters. One request can contain up to 100 queries
    :type body: list | bytes

    """
    body = [SearchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def search_query_get(request: web.Request, query, page=None, page_size=None) -> web.Response:
    """Search through all resources

    Searches through all resources and returns a JSON array with search results. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. The metadata of each resource need to be obtained through an appropriate method.

    :param query: The search query
    :type query: str
    :param page: Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    :type page: int
    :param page_size: The number of results to return per page. Can be any number between 10 and 100, default is 10.
    :type page_size: int

    """
    return web.Response(status=200)
