from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.transaction import Transaction
from openapi_server.models.transaction_list_result import TransactionListResult
from openapi_server import util


async def transactions_get(request: web.Request, billing_account_name, billing_profile_name, transaction_name, period_start_date, period_end_date, api_version) -> web.Response:
    """transactions_get

    Get the transaction.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param transaction_name: Transaction name.
    :type transaction_name: str
    :param period_start_date: Start date
    :type period_start_date: str
    :param period_end_date: End date
    :type period_end_date: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def transactions_list_by_billing_account(request: web.Request, billing_account_name, api_version, period_start_date, period_end_date, filter=None) -> web.Response:
    """transactions_list_by_billing_account

    Lists the transactions by billing account name for given start and end date.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param period_start_date: Start date
    :type period_start_date: str
    :param period_end_date: End date
    :type period_end_date: str
    :param filter: May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def transactions_list_by_billing_profile(request: web.Request, billing_account_name, billing_profile_name, api_version, period_start_date, period_end_date, filter=None) -> web.Response:
    """transactions_list_by_billing_profile

    Lists the transactions by billing profile name for given start date and end date.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param period_start_date: Start date
    :type period_start_date: str
    :param period_end_date: End date
    :type period_end_date: str
    :param filter: May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def transactions_list_by_customer(request: web.Request, billing_account_name, customer_name, api_version, period_start_date, period_end_date, filter=None) -> web.Response:
    """transactions_list_by_customer

    Lists the transactions by customer id for given start date and end date.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param period_start_date: Start date
    :type period_start_date: str
    :param period_end_date: End date
    :type period_end_date: str
    :param filter: May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def transactions_list_by_invoice_section(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, api_version, period_start_date, period_end_date, filter=None) -> web.Response:
    """transactions_list_by_invoice_section

    Lists the transactions by invoice section name for given start date and end date.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param period_start_date: Start date
    :type period_start_date: str
    :param period_end_date: End date
    :type period_end_date: str
    :param filter: May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)
