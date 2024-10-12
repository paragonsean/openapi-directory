from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_permissions_list_result import BillingPermissionsListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_permissions_list_by_billing_account(request: web.Request, api_version, billing_account_name) -> web.Response:
    """billing_permissions_list_by_billing_account

    Lists all billing permissions for the caller under a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str

    """
    return web.Response(status=200)


async def billing_permissions_list_by_billing_profile(request: web.Request, api_version, billing_account_name, billing_profile_name) -> web.Response:
    """billing_permissions_list_by_billing_profile

    Lists all billingPermissions for the caller has for a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str

    """
    return web.Response(status=200)


async def billing_permissions_list_by_customers(request: web.Request, api_version, billing_account_name, customer_name) -> web.Response:
    """billing_permissions_list_by_customers

    Lists all billing permissions for the caller under customer.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param customer_name: Customer Id.
    :type customer_name: str

    """
    return web.Response(status=200)


async def billing_permissions_list_by_invoice_sections(request: web.Request, api_version, billing_account_name, invoice_section_name) -> web.Response:
    """billing_permissions_list_by_invoice_sections

    Lists all billing permissions for the caller under invoice section.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param invoice_section_name: InvoiceSection Id.
    :type invoice_section_name: str

    """
    return web.Response(status=200)
