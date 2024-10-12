from typing import List, Dict
from aiohttp import web

from openapi_server.models.erskine_may_index_term_search_result_erskine_may_search import ErskineMayIndexTermSearchResultErskineMaySearch
from openapi_server.models.erskine_may_paragraph_search_result_erskine_may_search import ErskineMayParagraphSearchResultErskineMaySearch
from openapi_server.models.erskine_may_section_overview import ErskineMaySectionOverview
from openapi_server.models.erskine_may_section_search_result_erskine_may_search import ErskineMaySectionSearchResultErskineMaySearch
from openapi_server import util


async def api_search_index_term_search_results_search_term_get(request: web.Request, search_term, skip=None, take=None) -> web.Response:
    """Returns a list of index terms which contain the search term.

    

    :param search_term: Index terms which contain search term.
    :type search_term: str
    :param skip: The number of records to skip from the first, default is 0.
    :type skip: int
    :param take: The number of records to return, default is 20, maximum is 20.
    :type take: int

    """
    return web.Response(status=200)


async def api_search_paragraph_reference_get(request: web.Request, reference) -> web.Response:
    """Returns a section overview by reference.

    

    :param reference: Section overview by reference.
    :type reference: str

    """
    return web.Response(status=200)


async def api_search_paragraph_search_results_search_term_get(request: web.Request, search_term, skip=None, take=None) -> web.Response:
    """Returns a list of paragraphs which contain the search term.

    

    :param search_term: Paragraphs which contain search term in their content.
    :type search_term: str
    :param skip: The number of records to skip from the first, default is 0.
    :type skip: int
    :param take: The number of records to return, default is 20, maximum is 20.
    :type take: int

    """
    return web.Response(status=200)


async def api_search_section_search_results_search_term_get(request: web.Request, search_term, skip=None, take=None) -> web.Response:
    """Returns a list of sections which contain the search term.

    

    :param search_term: Sections which contain search term in their title.
    :type search_term: str
    :param skip: The number of records to skip from the first, default is 0.
    :type skip: int
    :param take: The number of records to return, default is 20, maximum is 20.
    :type take: int

    """
    return web.Response(status=200)
