from typing import List, Dict
from aiohttp import web

from openapi_server.models.erskine_may_index_term import ErskineMayIndexTerm
from openapi_server.models.erskine_may_index_term_search_result_erskine_may_search import ErskineMayIndexTermSearchResultErskineMaySearch
from openapi_server import util


async def api_index_term_browse_get(request: web.Request, start_letter=None, skip=None, take=None) -> web.Response:
    """Returns a list of index terms by start letter.

    

    :param start_letter: Index terms by start letter
    :type start_letter: str
    :param skip: The number of records to skip from the first, default is 0.
    :type skip: int
    :param take: The number of records to return, default is 20, maximum is 20.
    :type take: int

    """
    return web.Response(status=200)


async def api_index_term_index_term_id_get(request: web.Request, index_term_id) -> web.Response:
    """Returns an index term by id.

    

    :param index_term_id: Index term by if
    :type index_term_id: int

    """
    return web.Response(status=200)
