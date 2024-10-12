from typing import List, Dict
from aiohttp import web

from openapi_server.models.continuous_project_document import ContinuousProjectDocument
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_subjects import DocumentSubjects
from openapi_server.models.error import Error
from openapi_server.models.list_order_type import ListOrderType
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.progress import Progress
from openapi_server.models.regenerate_preview_response import RegeneratePreviewResponse
from openapi_server.models.use_as_draft_payload import UseAsDraftPayload
from openapi_server.models.use_as_regular_payload import UseAsRegularPayload
from openapi_server import util


async def get_all_document_subjects(request: web.Request, ) -> web.Response:
    """Get a list of subjects of projects

    Get a list of subjects of projects


    """
    return web.Response(status=200)


async def get_document(request: web.Request, document_id) -> web.Response:
    """View a single document

    View a single document from your MotaWord account with its translation info.

    :param document_id: Document ID or filename
    :type document_id: str

    """
    return web.Response(status=200)


async def get_document_progress(request: web.Request, document_id) -> web.Response:
    """View a document translation progress

    View the translation or proofreading progress of a document in your account. You can also track the progress of a document under the project that it was ordered with.

    :param document_id: Document ID
    :type document_id: 

    """
    return web.Response(status=200)


async def get_documents(request: web.Request, recent=None, search=None, type_filter=None, language_code=None, page=None, per_page=None, order_by=None, order_type=None, _with=None) -> web.Response:
    """View your documents

    View a list of files and documents that you have translations for. This endpoint lets you view your MotaWord account as a multilingual translated file repository, without needing to go through your projects to interact with files in them.

    :param recent: When true, this will return the most 4 recent active documents.
    :type recent: bool
    :param search: 
    :type search: str
    :param type_filter: 
    :type type_filter: str
    :param language_code: searches in source language of documents, in source and target languages of document&#39;s quote
    :type language_code: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param order_by: 
    :type order_by: str
    :param order_type: 
    :type order_type: dict | bytes
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    order_type = .from_dict(order_type)
    return web.Response(status=200)


async def get_similar_documents(request: web.Request, document_id, per_page=None, _with=None) -> web.Response:
    """Find documents similar to this document.

    Find documents similar to this document. Optionally, include translation information.

    :param document_id: Document ID
    :type document_id: int
    :param per_page: Determines the number of similar documents to return.
    :type per_page: int
    :param _with: Attach further information. Possible values &#39;preview&#39; to fetch temporary preview URLs. This is NOT recommended to be used with list calls. Only use with[]&#x3D;preview for single document/style guide calls.
    :type _with: List[str]

    """
    return web.Response(status=200)


async def get_user_documents(request: web.Request, user_id, recent=None, search=None, type_filter=None, language_code=None, page=None, per_page=None, order_by=None, order_type=None) -> web.Response:
    """Get a list of your documents

    Get a list of your documents

    :param user_id: User ID
    :type user_id: int
    :param recent: When true, this will return the most 4 recent active documents.
    :type recent: bool
    :param search: 
    :type search: str
    :param type_filter: 
    :type type_filter: str
    :param language_code: searches in source language of documents, in source and target languages of document&#39;s quote
    :type language_code: str
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param order_by: 
    :type order_by: str
    :param order_type: 
    :type order_type: dict | bytes

    """
    order_type = .from_dict(order_type)
    return web.Response(status=200)


async def regenerate_preview(request: web.Request, document_id) -> web.Response:
    """Regenerate preview and return preview URL for given file

    Regenerate preview and return preview URL for given file

    :param document_id: Document ID
    :type document_id: int

    """
    return web.Response(status=200)


async def use_as_draft(request: web.Request, document_id, body=None) -> web.Response:
    """Use the translation of given source manual document as manual draft source for the given target document.

    Use the translation of given source manual document as manual draft source for the given target document.

    :param document_id: Document ID
    :type document_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UseAsDraftPayload.from_dict(body)
    return web.Response(status=200)


async def use_as_regular(request: web.Request, document_id, body=None) -> web.Response:
    """Use the translation of the given manual document as a regular file.

    Use the translation of the given manual document as a regular file.

    :param document_id: Document ID
    :type document_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UseAsRegularPayload.from_dict(body)
    return web.Response(status=200)
