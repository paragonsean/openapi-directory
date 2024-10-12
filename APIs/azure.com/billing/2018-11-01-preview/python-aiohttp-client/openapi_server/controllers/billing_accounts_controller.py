from typing import List, Dict
from aiohttp import web

from openapi_server.models.billing_account import BillingAccount
from openapi_server.models.billing_account_list_result import BillingAccountListResult
from openapi_server.models.billing_account_update_properties import BillingAccountUpdateProperties
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def billing_accounts_get(request: web.Request, api_version, billing_account_name, expand=None) -> web.Response:
    """billing_accounts_get

    Get the billing account by id.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param expand: May be used to expand the invoiceSections and billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_accounts_list(request: web.Request, api_version, expand=None) -> web.Response:
    """billing_accounts_list

    Lists all billing accounts for which a user has access.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param expand: May be used to expand the invoiceSections and billingProfiles.
    :type expand: str

    """
    return web.Response(status=200)


async def billing_accounts_update(request: web.Request, api_version, billing_account_name, parameters) -> web.Response:
    """billing_accounts_update

    The operation to update a billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str
    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param parameters: Parameters supplied to the update billing account operation.
    :type parameters: dict | bytes

    """
    parameters = BillingAccountUpdateProperties.from_dict(parameters)
    return web.Response(status=200)
