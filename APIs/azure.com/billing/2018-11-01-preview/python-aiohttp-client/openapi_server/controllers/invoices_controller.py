from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice_list_result import InvoiceListResult
from openapi_server.models.invoice_summary import InvoiceSummary
from openapi_server import util


async def invoices_get(request: web.Request, api_version, billing_account_name, billing_profile_name, invoice_name) -> web.Response:
    """invoices_get

    Get the invoice by name.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_name: Invoice Id.
    :type invoice_name: str

    """
    return web.Response(status=200)


async def invoices_list_by_billing_account_name(request: web.Request, api_version, billing_account_name, period_start_date, period_end_date) -> web.Response:
    """invoices_list_by_billing_account_name

    List of invoices for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param period_start_date: Invoice period start date.
    :type period_start_date: str
    :param period_end_date: Invoice period end date.
    :type period_end_date: str

    """
    return web.Response(status=200)


async def invoices_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name, period_start_date, period_end_date) -> web.Response:
    """invoices_list_by_billing_profile

    List of invoices for a billing profile.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param period_start_date: Invoice period start date.
    :type period_start_date: str
    :param period_end_date: Invoice period end date.
    :type period_end_date: str

    """
    return web.Response(status=200)
