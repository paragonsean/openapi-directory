from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_invoice_create_dto import CustomerInvoiceCreateDTO
from openapi_server.models.customer_invoice_create_result_dto import CustomerInvoiceCreateResultDTO
from openapi_server.models.customer_invoice_dto import CustomerInvoiceDTO
from openapi_server.models.customer_invoice_dates_dto import CustomerInvoiceDatesDTO
from openapi_server.models.download_documents_request_dto import DownloadDocumentsRequestDTO
from openapi_server.models.payment_dto import PaymentDTO
from openapi_server.models.payment_terms_dto import PaymentTermsDTO
from openapi_server.models.send_reminders_request_dto import SendRemindersRequestDTO
from openapi_server.models.send_reminders_response_dto import SendRemindersResponseDTO
from openapi_server.models.url_result_dto import UrlResultDTO
from openapi_server import util


async def create1(request: web.Request, body) -> web.Response:
    """Creates a new invoice.

    Creates a new invoice from tasks. Tasks are grouped by client and currency, therefore multiple invoices can be created.If any of the tasks cannot be invoiced (ie. it is already invoiced, not invoiceable, not associated with a project) then an error is reported.

    :param body: Created new invoice.
    :type body: dict | bytes

    """
    body = CustomerInvoiceCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_payment(request: web.Request, invoice_id, body) -> web.Response:
    """Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

    Adds a new payment to the client invoice. The invoice payment status (Not Paid, Partially Paid, Fully Paid) is automatically recalculated.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int
    :param body: New payment.
    :type body: dict | bytes

    """
    body = PaymentDTO.from_dict(body)
    return web.Response(status=200)


async def delete1(request: web.Request, invoice_id) -> web.Response:
    """Removes a client invoice.

    Removes a client invoice.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def delete2(request: web.Request, payment_id) -> web.Response:
    """Removes a customer payment.

    Removes a customer payment.

    :param payment_id: customer payment&#39;s internal identifier
    :type payment_id: int

    """
    return web.Response(status=200)


async def download_documents(request: web.Request, body) -> web.Response:
    """Generates client invoices&#39; documents.

    Generates client invoices&#39; documents.

    :param body: Generated client invoices documents.
    :type body: dict | bytes

    """
    body = DownloadDocumentsRequestDTO.from_dict(body)
    return web.Response(status=200)


async def duplicate(request: web.Request, invoice_id) -> web.Response:
    """Duplicate client invoice.

    Duplicate client invoice.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def duplicate_as_pro_forma(request: web.Request, invoice_id) -> web.Response:
    """Duplicate client invoice as pro forma.

    Duplicate client invoice as pro forma.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_all(request: web.Request, updated_since=None) -> web.Response:
    """Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

    Lists all client invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

    :param updated_since: only client invoices modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_all_ids(request: web.Request, updated_since=None) -> web.Response:
    """Returns client invoices&#39; internal identifiers.

    Returns client invoices&#39; internal identifiers.

    :param updated_since: only client invoices modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id(request: web.Request, invoice_id, embed=None) -> web.Response:
    """Returns client invoice details.

    Returns client invoice details.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int
    :param embed: list of adittional fields which should be embedded in the response (ie. tasks)
    :type embed: str

    """
    return web.Response(status=200)


async def get_dates(request: web.Request, invoice_id) -> web.Response:
    """Returns dates of a given client invoice.

    Returns dates of a given client invoice.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_document(request: web.Request, invoice_id) -> web.Response:
    """Generates client invoice document (PDF).

    Generates client invoice document (PDF).

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_payment_terms(request: web.Request, invoice_id) -> web.Response:
    """Returns payment terms of a given client invoice.

    Returns payment terms of a given client invoice.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_payments(request: web.Request, invoice_id) -> web.Response:
    """Returns all payments for the client invoice.

    Returns all payments for the client invoice.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def send_reminder(request: web.Request, invoice_id) -> web.Response:
    """Sends reminder.

    Sends reminder.

    :param invoice_id: client invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def send_reminders(request: web.Request, body) -> web.Response:
    """Sends reminders. Returns number of sent e-mails.

    Sends reminders. Returns number of sent e-mails.

    :param body: Number of sent e-mails.
    :type body: dict | bytes

    """
    body = SendRemindersRequestDTO.from_dict(body)
    return web.Response(status=200)
