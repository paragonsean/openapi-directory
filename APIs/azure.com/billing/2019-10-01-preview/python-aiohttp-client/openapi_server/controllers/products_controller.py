from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.product import Product
from openapi_server.models.products_list_result import ProductsListResult
from openapi_server.models.transfer_product_request_properties import TransferProductRequestProperties
from openapi_server.models.update_auto_renew_operation import UpdateAutoRenewOperation
from openapi_server.models.update_auto_renew_request import UpdateAutoRenewRequest
from openapi_server import util


async def products_get(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, product_name, api_version) -> web.Response:
    """products_get

    Get a single product by name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param product_name: Invoice Id.
    :type product_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_get_by_customer(request: web.Request, billing_account_name, customer_name, product_name, api_version) -> web.Response:
    """products_get_by_customer

    Get a customer&#39;s product by name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param product_name: Invoice Id.
    :type product_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_list_by_billing_account(request: web.Request, billing_account_name, api_version, filter=None) -> web.Response:
    """products_list_by_billing_account

    Lists products by billing account name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param filter: May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def products_list_by_customer(request: web.Request, billing_account_name, customer_name, api_version, filter=None) -> web.Response:
    """products_list_by_customer

    Lists products by customer id.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer name.
    :type customer_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param filter: May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def products_list_by_invoice_section(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, api_version, filter=None) -> web.Response:
    """products_list_by_invoice_section

    Lists products by invoice section name.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param filter: May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:).
    :type filter: str

    """
    return web.Response(status=200)


async def products_transfer(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, product_name, api_version, parameters) -> web.Response:
    """products_transfer

    The operation to transfer a Product to another invoice section.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param product_name: Invoice Id.
    :type product_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param parameters: Parameters supplied to the Transfer Product operation.
    :type parameters: dict | bytes

    """
    parameters = TransferProductRequestProperties.from_dict(parameters)
    return web.Response(status=200)


async def products_update_auto_renew_by_invoice_section(request: web.Request, billing_account_name, billing_profile_name, invoice_section_name, product_name, api_version, body) -> web.Response:
    """products_update_auto_renew_by_invoice_section

    Cancel auto renew for product by product id and invoice section name

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str
    :param product_name: Invoice Id.
    :type product_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param body: Update auto renew request parameters.
    :type body: dict | bytes

    """
    body = UpdateAutoRenewRequest.from_dict(body)
    return web.Response(status=200)
