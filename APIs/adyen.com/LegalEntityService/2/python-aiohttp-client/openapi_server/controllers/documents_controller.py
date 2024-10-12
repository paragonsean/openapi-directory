from typing import List, Dict
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.service_error import ServiceError
from openapi_server import util


async def delete_documents_id(request: web.Request, id) -> web.Response:
    """Delete a document

    Deletes a document.

    :param id: The unique identifier of the document to be deleted.
    :type id: str

    """
    return web.Response(status=200)


async def get_documents_id(request: web.Request, id, skip_content=None) -> web.Response:
    """Get a document

    Returns a document.

    :param id: The unique identifier of the document.
    :type id: str
    :param skip_content: Do not load document content while fetching the document.
    :type skip_content: bool

    """
    return web.Response(status=200)


async def patch_documents_id(request: web.Request, id, x_requested_verification_code=None, body=None) -> web.Response:
    """Update a document

    Updates a document.   &gt;You can upload a maximum of 15 pages for photo IDs.

    :param id: The unique identifier of the document to be updated.
    :type id: str
    :param x_requested_verification_code: Use the requested verification code 0_0001 to resolve any suberrors associated with the document. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = Document.from_dict(body)
    return web.Response(status=200)


async def post_documents(request: web.Request, x_requested_verification_code=None, body=None) -> web.Response:
    """Upload a document for verification checks

    Uploads a document for verification checks.   Adyen uses the information from the [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities) to run automated verification checks. If these checks fail, you will be notified to provide additional documents.   You should only upload documents when Adyen requests additional information for the legal entity.   &gt;You can upload a maximum of 15 pages for photo IDs.

    :param x_requested_verification_code: Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
    :type x_requested_verification_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = Document.from_dict(body)
    return web.Response(status=200)
