from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.payment_methods_list_result import PaymentMethodsListResult
from openapi_server import util


async def payment_methods_list_by_billing_account(request: web.Request, billing_account_name, api_version) -> web.Response:
    """payment_methods_list_by_billing_account

    Lists the Payment Methods by billing account Id.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)


async def payment_methods_list_by_billing_profile(request: web.Request, billing_account_name, billing_profile_name, api_version) -> web.Response:
    """payment_methods_list_by_billing_profile

    Lists the Payment Methods by billing profile Id.

    :param billing_account_name: billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-10-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
