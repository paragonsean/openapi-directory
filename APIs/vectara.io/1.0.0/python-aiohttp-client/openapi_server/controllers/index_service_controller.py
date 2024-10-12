from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_upload200_response import FileUpload200Response
from openapi_server.models.file_upload400_response import FileUpload400Response
from openapi_server.models.googlerpc_status import GooglerpcStatus
from openapi_server.models.vectara_delete_document_request import VectaraDeleteDocumentRequest
from openapi_server.models.vectara_index_document_request import VectaraIndexDocumentRequest
from openapi_server.models.vectara_index_document_response import VectaraIndexDocumentResponse
from openapi_server import util


async def delete(request: web.Request, customer_id, body) -> web.Response:
    """delete

    Delete

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = VectaraDeleteDocumentRequest.from_dict(body)
    return web.Response(status=200)


async def file_upload(request: web.Request, c, o, d=None, doc_metadata=None, file=None) -> web.Response:
    """file_upload

    File Upload

    :param c: Customer ID
    :type c: int
    :param o: Corpus ID
    :type o: int
    :param d: If true, the server returns the extracted document that was indexed
    :type d: bool
    :param doc_metadata: A JSON string of any additional metadata you want attached to the file.
    :type doc_metadata: str
    :param file: The file to be indexed into Vectara.
    :type file: str

    """
    return web.Response(status=200)


async def index(request: web.Request, customer_id, body) -> web.Response:
    """index

    Index

    :param customer_id: The Customer ID to use for the request.
    :type customer_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = VectaraIndexDocumentRequest.from_dict(body)
    return web.Response(status=200)
