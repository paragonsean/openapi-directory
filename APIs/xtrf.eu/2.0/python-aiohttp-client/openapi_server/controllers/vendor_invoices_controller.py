from typing import List, Dict
from aiohttp import web

from openapi_server.models.payment_dto import PaymentDTO
from openapi_server.models.provider_invoice_create_dto import ProviderInvoiceCreateDTO
from openapi_server.models.provider_invoice_create_result_dto import ProviderInvoiceCreateResultDTO
from openapi_server.models.provider_invoice_dto import ProviderInvoiceDTO
from openapi_server.models.status_request_dto import StatusRequestDTO
from openapi_server.models.url_result_dto import UrlResultDTO
from openapi_server import util


async def create4(request: web.Request, body) -> web.Response:
    """Creates a new invoice.

    Creates a new invoice from jobs. Jobs are grouped by provider and currency, therefore multiple invoices can be created.If any of the jobs cannot be invoiced (ie. it is already invoiced) then an error is reported.

    :param body: Created new invoice.
    :type body: dict | bytes

    """
    body = ProviderInvoiceCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_payment1(request: web.Request, invoice_id, body) -> web.Response:
    """Creates a new payment on the vendor account and assigns the payment to the invoice.

    Creates a new payment on the vendor account and assigns the payment to the invoice.

    :param invoice_id: vendor invoice&#39;s internal identifier
    :type invoice_id: int
    :param body: New payment.
    :type body: dict | bytes

    """
    body = PaymentDTO.from_dict(body)
    return web.Response(status=200)


async def delete6(request: web.Request, invoice_id) -> web.Response:
    """Removes a provider invoice.

    Removes a provider invoice.

    :param invoice_id: provider invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def delete7(request: web.Request, payment_id) -> web.Response:
    """Removes a provider payment.

    Removes a provider payment.

    :param payment_id: provider payment&#39;s internal identifier
    :type payment_id: int

    """
    return web.Response(status=200)


async def get_all2(request: web.Request, updated_since=None) -> web.Response:
    """Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

    Lists all vendor invoices in all statuses (including not ready and drafts) that have been updated since a specific date.

    :param updated_since: only vendor invoices modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_all_ids3(request: web.Request, updated_since=None) -> web.Response:
    """Returns vendor invoices&#39; internal identifiers.

    Returns vendor invoices&#39; internal identifiers.

    :param updated_since: only vendor invoices modified since this timestamp
    :type updated_since: int

    """
    return web.Response(status=200)


async def get_by_id3(request: web.Request, invoice_id) -> web.Response:
    """Returns provider invoice details.

    Returns provider invoice details.

    :param invoice_id: provider invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_document1(request: web.Request, invoice_id) -> web.Response:
    """Generates provider invoice document (PDF).

    Generates provider invoice document (PDF).

    :param invoice_id: provider invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def get_payments1(request: web.Request, invoice_id) -> web.Response:
    """Returns all payments for the vendor invoice.

    Returns all payments for the vendor invoice.

    :param invoice_id: vendor invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def send(request: web.Request, invoice_id) -> web.Response:
    """Sends a provider invoice.

    Sends a provider invoice.

    :param invoice_id: provider invoice&#39;s internal identifier
    :type invoice_id: int

    """
    return web.Response(status=200)


async def set_status(request: web.Request, invoice_id, body) -> web.Response:
    """Changes invoice status to given status.

    Changes invoice status to given status.

    :param invoice_id: provider invoice&#39;s internal identifier
    :type invoice_id: int
    :param body: Changed invoice status to given status.
    :type body: dict | bytes

    """
    body = StatusRequestDTO.from_dict(body)
    return web.Response(status=200)
