from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_updates import DocumentUpdates
from openapi_server.models.document_upload_request import DocumentUploadRequest
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus
from openapi_server import util


async def create_project_document(request: web.Request, project_id, body=None) -> web.Response:
    """Upload a new document

    Upload a new document

    :param project_id: Project ID
    :type project_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DocumentUpdates.from_dict(body)
    return web.Response(status=200)


async def delete_project_document(request: web.Request, project_id, document_id) -> web.Response:
    """Delete the document

    Delete the document

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def download_project_document(request: web.Request, project_id, document_id) -> web.Response:
    """Download a project source document

    Download an actual source file you uploaded to be translated in your project.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def download_translated_document_for_language(request: web.Request, project_id, document_id, language, certified=None) -> web.Response:
    """Download translated document

    Download translated document in the given target language.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int
    :param language: Target language code.
    :type language: str
    :param certified: Download certified translation
    :type certified: bool

    """
    return web.Response(status=200)


async def get_project_document(request: web.Request, project_id, document_id, _with=None) -> web.Response:
    """View a project source document

    View the details of a source file you uploaded to be translated in your project.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    return web.Response(status=200)


async def get_project_documents(request: web.Request, project_id, _with=None) -> web.Response:
    """View project source documents

    Get a list of source files you uploaded to be translated in your project.

    :param project_id: Project ID
    :type project_id: int
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    return web.Response(status=200)


async def update_project_document(request: web.Request, project_id, document_id, body=None) -> web.Response:
    """Update the document.

    Update the document. File name and contents will replaced with the new one.

    :param project_id: Project ID
    :type project_id: int
    :param document_id: Document ID
    :type document_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DocumentUploadRequest.from_dict(body)
    return web.Response(status=200)
