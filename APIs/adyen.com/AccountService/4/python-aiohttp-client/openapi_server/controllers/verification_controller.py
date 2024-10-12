from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_bank_account_request import DeleteBankAccountRequest
from openapi_server.models.delete_legal_arrangement_request import DeleteLegalArrangementRequest
from openapi_server.models.delete_shareholder_request import DeleteShareholderRequest
from openapi_server.models.delete_signatories_request import DeleteSignatoriesRequest
from openapi_server.models.generic_response import GenericResponse
from openapi_server.models.get_uploaded_documents_request import GetUploadedDocumentsRequest
from openapi_server.models.get_uploaded_documents_response import GetUploadedDocumentsResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.update_account_holder_response import UpdateAccountHolderResponse
from openapi_server.models.upload_document_request import UploadDocumentRequest
from openapi_server import util


async def post_delete_bank_accounts(request: web.Request, body=None) -> web.Response:
    """Delete bank accounts

    Deletes bank accounts associated with an account holder. 

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteBankAccountRequest.from_dict(body)
    return web.Response(status=200)


async def post_delete_legal_arrangements(request: web.Request, body=None) -> web.Response:
    """Delete legal arrangements

    Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteLegalArrangementRequest.from_dict(body)
    return web.Response(status=200)


async def post_delete_shareholders(request: web.Request, body=None) -> web.Response:
    """Delete shareholders

    Deletes shareholders associated with an account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteShareholderRequest.from_dict(body)
    return web.Response(status=200)


async def post_delete_signatories(request: web.Request, body=None) -> web.Response:
    """Delete signatories

    Deletes signatories associated with an account holder.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteSignatoriesRequest.from_dict(body)
    return web.Response(status=200)


async def post_get_uploaded_documents(request: web.Request, body=None) -> web.Response:
    """Get documents

    Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process). 

    :param body: 
    :type body: dict | bytes

    """
    body = GetUploadedDocumentsRequest.from_dict(body)
    return web.Response(status=200)


async def post_upload_document(request: web.Request, body=None) -> web.Response:
    """Upload a document

    Uploads a document for an account holder. Adyen uses the documents during the [verification process](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process).

    :param body: 
    :type body: dict | bytes

    """
    body = UploadDocumentRequest.from_dict(body)
    return web.Response(status=200)
