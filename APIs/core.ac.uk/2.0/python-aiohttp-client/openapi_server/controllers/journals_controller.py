from typing import List, Dict
from aiohttp import web

from openapi_server.models.journal_response import JournalResponse
from openapi_server.models.journal_search_response import JournalSearchResponse
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def get_journal_by_issn(request: web.Request, issn) -> web.Response:
    """Find journal by ISSN

    Returns a journal with given ISSN identifier.

    :param issn: ISSN identifier of journal that needs to be fetched.
    :type issn: str

    """
    return web.Response(status=200)


async def get_journal_by_issn_batch(request: web.Request, body) -> web.Response:
    """Batch operation for retrieving journals by ISSN

    Method accepts a JSON array of ISSNs and retrieves a list of journals.

    :param body: JSON array with ISSNs of journals that need to be fetched
    :type body: List[str]

    """
    return web.Response(status=200)


async def journals_search_post(request: web.Request, body) -> web.Response:
    """Batch operation for search through journals

    Method accepts a JSON array of search queries and parameters. It then searches through all journals and returns a JSON array of search results for each of the queries. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

    :param body: JSON array with search queries and parameters. One request can contain up to 100 queries.
    :type body: list | bytes

    """
    body = [SearchRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def journals_search_query_get(request: web.Request, query, page=None, page_size=None) -> web.Response:
    """Search through journals

    Searches through all journals and returns a JSON array of search results. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

    :param query: Search query
    :type query: str
    :param page: Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    :type page: int
    :param page_size: The number of results to return per page. Can be any number between 10 and 100, default is 10.
    :type page_size: int

    """
    return web.Response(status=200)
