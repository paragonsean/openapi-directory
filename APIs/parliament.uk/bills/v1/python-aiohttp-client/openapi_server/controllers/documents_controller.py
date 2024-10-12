from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.publication_document import PublicationDocument
from openapi_server import util


async def api_v1_publications_publication_id_documents_document_id_download_get(request: web.Request, publication_id, document_id) -> web.Response:
    """Return a document.

    

    :param publication_id: Document with publication Id specified
    :type publication_id: int
    :param document_id: Document with Id specified
    :type document_id: int

    """
    return web.Response(status=200)


async def api_v1_publications_publication_id_documents_document_id_get(request: web.Request, publication_id, document_id) -> web.Response:
    """Return information on a document.

    

    :param publication_id: Document with publication Id specified
    :type publication_id: int
    :param document_id: Document with Id specified
    :type document_id: int

    """
    return web.Response(status=200)
