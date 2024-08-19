from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error import ClientError
from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.document import Document
from openapi_server.models.document_insert import DocumentInsert
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_public_url import DocumentPublicUrl
from openapi_server.models.online_szamla_status import OnlineSzamlaStatus
from openapi_server.models.payment_history import PaymentHistory
from openapi_server.models.payment_method import PaymentMethod
from openapi_server.models.payment_status import PaymentStatus
from openapi_server.models.send_document import SendDocument
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def cancel_document(request: web.Request, id) -> web.Response:
    """Cancel a document

    Cancel a document. Returns a cancellation document object if the cancellation is succeded.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def create_document(request: web.Request, body) -> web.Response:
    """Create a document

    Create a new document. Returns a document object if the create is succeded.

    :param body: DocumentInsert object that you would like to store.
    :type body: dict | bytes

    """
    body = DocumentInsert.from_dict(body)
    return web.Response(status=200)


async def create_document_from_proforma(request: web.Request, id) -> web.Response:
    """Create a document from proforma.

    Create a new document from proforma. Returns a document object if the create is succeded.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def delete_payment(request: web.Request, id) -> web.Response:
    """Delete all payment history on document

    Delete all exist payment history on document.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def download_document(request: web.Request, id) -> web.Response:
    """Download a document in PDF format.

    Download a document. Returns a document in PDF format.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_document(request: web.Request, id) -> web.Response:
    """Retrieve a document

    Retrieves the details of an existing document.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_online_szamla_status(request: web.Request, id) -> web.Response:
    """Retrieve a document Online Számla status

    Retrieves the details of an existing document status.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_payment(request: web.Request, id) -> web.Response:
    """Retrieve a payment histroy

    Retrieves the details of payment history an existing document.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_public_url(request: web.Request, id) -> web.Response:
    """Retrieve a document download public url.

    Retrieves public url to download an existing document.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def list_document(request: web.Request, page=None, per_page=None, block_id=None, partner_id=None, payment_method=None, payment_status=None, start_date=None, end_date=None, start_number=None, end_number=None, start_year=None, end_year=None) -> web.Response:
    """List all documents

    Returns a list of your documents. The documents are returned sorted by creation date, with the most recent documents appearing first.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int
    :param block_id: Filter documents by the identifier of your DocumentBlock.
    :type block_id: int
    :param partner_id: Filter documents by the identifier of your Partner.
    :type partner_id: int
    :param payment_method: Filter documents by PaymentMethod value.
    :type payment_method: dict | bytes
    :param payment_status: Filter documents by PaymentStatus value.
    :type payment_status: dict | bytes
    :param start_date: Filter documents by date.
    :type start_date: str
    :param end_date: Filter documents by date.
    :type end_date: str
    :param start_number: Starting number of the document, should not contain year or any other formatting. Required if &#x60;start_year&#x60; given
    :type start_number: int
    :param end_number: Ending number of the document, should not contain year or any other formatting. Required if &#x60;end_year&#x60; given
    :type end_number: int
    :param start_year: Year for &#x60;start_number&#x60; parameter. Required if &#x60;start_number&#x60; given.
    :type start_year: int
    :param end_year: Year for &#x60;end_number&#x60; parameter. Required if &#x60;end_number&#x60; given.
    :type end_year: int

    """
    payment_method = .from_dict(payment_method)
    payment_status = .from_dict(payment_status)
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def send_document(request: web.Request, id, body=None) -> web.Response:
    """Send invoice to given email adresses.

    Returns a list of emails, where the invoice is sent.

    :param id: 
    :type id: int
    :param body: List of email-s where you want to send the invoice.
    :type body: dict | bytes

    """
    body = SendDocument.from_dict(body)
    return web.Response(status=200)


async def update_payment(request: web.Request, id, body) -> web.Response:
    """Update payment history

    Update payment history an existing document. Returns a payment history object if the update is succeded.

    :param id: 
    :type id: int
    :param body: Payment history object that you would like to update.
    :type body: list | bytes

    """
    body = [PaymentHistory.from_dict(d) for d in body]
    return web.Response(status=200)
