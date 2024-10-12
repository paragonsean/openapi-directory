from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_account import BillingAccount
from openapi_server.models.billing_account_list_result import BillingAccountListResult
from openapi_server.models.billing_account_update_request import BillingAccountUpdateRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.invoice_section_list_with_create_sub_permission_result import InvoiceSectionListWithCreateSubPermissionResult
from openapi_server import util


async def billing_accounts_get(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """billing_accounts_get

    Get the billing account by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the address, invoiceSections and billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_accounts_list(request: web.Request, api_version, expand=None) -> web.Response:
    """billing_accounts_list

    Lists all billing accounts for a user which he has access to.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param expand: May be used to expand the address, invoiceSections and billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_accounts_list_invoice_sections_by_create_subscription_permission(request: web.Request, api_version, billing_account_name) -> web.Response:
    """billing_accounts_list_invoice_sections_by_create_subscription_permission

    Lists all invoice sections with create subscription permission for a user.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str

    """
    return web.Response(status=200)


async def billing_accounts_update(request: web.Request, api_version, billing_account_name, parameters) -> web.Response:
    """billing_accounts_update

    The operation to update a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str
    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param parameters: Request parameters supplied to the update billing account operation.
    :type parameters: dict | bytes

    """
    parameters = BillingAccountUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
