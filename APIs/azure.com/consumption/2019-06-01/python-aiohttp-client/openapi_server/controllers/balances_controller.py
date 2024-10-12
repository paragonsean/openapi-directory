from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance import Balance
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def balances_get_by_billing_account(request: web.Request, api_version, billing_account_id) -> web.Response:
    """balances_get_by_billing_account

    Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-06-01.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)


async def balances_get_for_billing_period_by_billing_account(request: web.Request, api_version, billing_account_id, billing_period_name) -> web.Response:
    """balances_get_for_billing_period_by_billing_account

    Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-06-01.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str

    """
    return web.Response(status=200)
