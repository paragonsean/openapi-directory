from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.facet import Facet
from openapi_server import util


async def facets_facet_get(request: web.Request, facet, scope, doc_type, term=None, offset=None, limit=None) -> web.Response:
    """Returns facets

    

    :param facet: The facet to search for
    :type facet: str
    :param scope: The scope of the result set, i.e. &#39;indices&#39; or a WeGA ID
    :type scope: str
    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param term: The search term to be looked for in the facet&#39;s label
    :type term: str
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)
