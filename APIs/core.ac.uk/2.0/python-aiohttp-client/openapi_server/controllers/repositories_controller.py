from typing import List, Dict
from aiohttp import web

from openapi_server.models.repository_response import RepositoryResponse
from openapi_server.models.repository_search_response import RepositorySearchResponse
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def get_repository_by_id(request: web.Request, repository_id, stats=None, deposit_history=None, deposit_history_cumulative=None) -> web.Response:
    """Get repository by CORE repository ID

    Method will retrieve a repository based on given CORE repository ID.

    :param repository_id: CORE repository ID of the article that needs to be fetched.
    :type repository_id: int
    :param stats: Whether to retrieve statistics about the repository. The default value is false
    :type stats: bool
    :param deposit_history: Returns deposit history over time
    :type deposit_history: bool
    :param deposit_history_cumulative: Returns deposit history over time
    :type deposit_history_cumulative: bool

    """
    return web.Response(status=200)


async def get_repository_by_id_batch(request: web.Request, body, stats=None, deposit_history=None, deposit_history_cumulative=None) -> web.Response:
    """Batch operation for retrieving repositories by CORE repository ID

    Method accepts a JSON array of CORE repository IDs and retrieves a list of repositories. The response array is ordered based on the order of the IDs in the request array. The maximum number of IDs in request is 100.

    :param body: JSON array with CORE repository IDs of repositories that need to be fetched
    :type body: List[int]
    :param stats: Whether to retrieve statistics about the repository. The default value is false
    :type stats: bool
    :param deposit_history: Returns deposit history over time
    :type deposit_history: bool
    :param deposit_history_cumulative: Returns deposit history over time
    :type deposit_history_cumulative: bool

    """
    return web.Response(status=200)


async def repositories_search_post(request: web.Request, body, stats=None, deposit_history=None, deposit_history_cumulative=None) -> web.Response:
    """Batch operation for searching through repositories

    Method accepts a JSON array of search queries and parameters. It then searches through all repositories and returns a JSON array of search results for each of the queries. Method searches through all repository fields.

    :param body: JSON array with search queries and parameters. One request can contain up to 100 queries
    :type body: list | bytes
    :param stats: Whether to retrieve statistics about the repository. The default value is false
    :type stats: bool
    :param deposit_history: Returns deposit history over time
    :type deposit_history: bool
    :param deposit_history_cumulative: Returns deposit history over time
    :type deposit_history_cumulative: bool

    """
    body = [SearchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def repositories_search_query_get(request: web.Request, query, page=None, page_size=None, stats=None, deposit_history=None, deposit_history_cumulative=None) -> web.Response:
    """Search through all repositories

    Searches through all repositories and returns a JSON array with search results. Method searches through all repository fields.

    :param query: The search query
    :type query: str
    :param page: Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    :type page: int
    :param page_size: The number of results to return per page. Can be any number between 10 and 100, default is 10.
    :type page_size: int
    :param stats: Whether to retrieve statistics about the repository. The default value is false
    :type stats: bool
    :param deposit_history: Returns deposit history over time
    :type deposit_history: bool
    :param deposit_history_cumulative: Returns deposit history over time
    :type deposit_history_cumulative: bool

    """
    return web.Response(status=200)
