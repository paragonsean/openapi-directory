from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.error import Error
from openapi_server import util


async def search_entity_get(request: web.Request, doc_type=None, q=None, offset=None, limit=None) -> web.Response:
    """Search for a WeGA entity

    This endpoint returns the search results for an entity&#39;s name or title. 

    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param q: The query string
    :type q: str
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)
