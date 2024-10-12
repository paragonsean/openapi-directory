from typing import List, Dict
from aiohttp import web

from openapi_server.models.code_sample import CodeSample
from openapi_server.models.error import Error
from openapi_server import util


async def code_find_by_element_element_get(request: web.Request, element, namespace=None, doc_type=None, offset=None, limit=None) -> web.Response:
    """Finds code samples by XML element

    

    :param element: The XML element to search for
    :type element: str
    :param namespace: The element namespace. Defaults to the TEI namespace
    :type namespace: str
    :param doc_type: The WeGA document type
    :type doc_type: List[str]
    :param offset: Position of first item to retrieve (starting from 1)
    :type offset: int
    :param limit: Number of items to retrieve (200 max)
    :type limit: int

    """
    return web.Response(status=200)
