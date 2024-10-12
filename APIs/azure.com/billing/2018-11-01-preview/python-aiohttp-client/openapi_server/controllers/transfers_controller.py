from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.initiate_transfer_request import InitiateTransferRequest
from openapi_server.models.transfer_details import TransferDetails
from openapi_server.models.transfer_details_list_result import TransferDetailsListResult
from openapi_server import util


async def transfers_cancel(request: web.Request, billing_account_name, invoice_section_name, transfer_name) -> web.Response:
    """transfers_cancel

    Cancels the transfer for given transfer Id.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param transfer_name: Transfer Name.
    :type transfer_name: str

    """
    return web.Response(status=200)


async def transfers_get(request: web.Request, billing_account_name, invoice_section_name, transfer_name) -> web.Response:
    """transfers_get

    Gets the transfer details for given transfer Id.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param transfer_name: Transfer Name.
    :type transfer_name: str

    """
    return web.Response(status=200)


async def transfers_initiate(request: web.Request, billing_account_name, invoice_section_name, body) -> web.Response:
    """transfers_initiate

    Initiates the request to transfer the legacy subscriptions or RIs.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param body: Initiate transfer parameters.
    :type body: dict | bytes

    """
    body = InitiateTransferRequest.from_dict(body)
    return web.Response(status=200)


async def transfers_list(request: web.Request, billing_account_name, invoice_section_name) -> web.Response:
    """transfers_list

    Lists all transfer&#39;s details initiated from given invoice section.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str

    """
    return web.Response(status=200)
