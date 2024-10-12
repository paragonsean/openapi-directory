from typing import List, Dict
from aiohttp import web

from openapi_server.models.available_balance import AvailableBalance
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def available_balances_get_by_billing_profile(request: web.Request, billing_account_name, billing_profile_name, api_version) -> web.Response:
    """available_balances_get_by_billing_profile

    The latest available credit balance for a given billingAccountName and billingProfileName.

    :param billing_account_name: Billing Account Id.
    :type billing_account_name: str
    :param billing_profile_name: Billing Profile Id.
    :type billing_profile_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview.
    :type api_version: str

    """
    return web.Response(status=200)
