from typing import List, Dict
from aiohttp import web

from openapi_server.models.document_download_response import DocumentDownloadResponse
from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.yodlee_error import YodleeError
from openapi_server import util


async def delete_document(request: web.Request, document_id) -> web.Response:
    """Delete Document

    The delete document service allows the consumer to delete a document. The deleted document will not be returned in the get documents API. The HTTP response code is 204 (success without content).&lt;br&gt;Documents can be deleted only if the document related dataset attributes are subscribed.&lt;br&gt;

    :param document_id: documentId
    :type document_id: str

    """
    return web.Response(status=200)


async def download_document(request: web.Request, document_id) -> web.Response:
    """Download a Document

    The get document details service allows consumers to download a document. The document is provided in base64.&lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

    :param document_id: documentId
    :type document_id: str

    """
    return web.Response(status=200)


async def get_documents(request: web.Request, keyword=None, account_id=None, doc_type=None, from_date=None, to_date=None) -> web.Response:
    """Get Documents

    The get documents service allows customers to search or retrieve metadata related to documents. &lt;br&gt;The API returns the document as per the input parameters passed. If no date range is provided then all downloaded documents will be retrieved. Details of deleted documents or documents associated to closed providerAccount will not be returned. &lt;br&gt;This API is a premium service which requires subscription in advance to use.  Please contact Yodlee Client Services for more information. &lt;br&gt;

    :param keyword: The string used to search a document by its name.
    :type keyword: str
    :param account_id: The unique identifier of an account. Retrieve documents for a given accountId.
    :type account_id: str
    :param doc_type: Accepts only one of the following valid document types: STMT, TAX, and EBILL.
    :type doc_type: str
    :param from_date: The date from which documents have to be retrieved.
    :type from_date: str
    :param to_date: The date to which documents have to be retrieved.
    :type to_date: str

    """
    return web.Response(status=200)
