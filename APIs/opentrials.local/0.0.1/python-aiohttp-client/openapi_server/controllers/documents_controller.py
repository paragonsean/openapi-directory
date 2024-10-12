from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_document(request: web.Request, id) -> web.Response:
    """get_document

    Returns details of a document

    :param id: ID of the document
    :type id: str

    """
    return web.Response(status=200)


async def list_documents(request: web.Request, page=None, per_page=None) -> web.Response:
    """list_documents

    Returns documents

    :param page: The page number
    :type page: int
    :param per_page: Number of items per page
    :type per_page: int

    """
    return web.Response(status=200)
