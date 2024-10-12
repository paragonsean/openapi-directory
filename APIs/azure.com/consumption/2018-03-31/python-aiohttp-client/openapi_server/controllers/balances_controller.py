from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance import Balance
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def get_balances_by_billing_account(request: web.Request, api_version, billing_account_id) -> web.Response:
    """get_balances_by_billing_account

    Gets the balances for a scope by billingAccountId. Balances are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)


async def get_balances_by_billing_account_by_billing_period(request: web.Request, api_version, billing_account_id, billing_period_name) -> web.Response:
    """get_balances_by_billing_account_by_billing_period

    Gets the balances for a scope by billing period and billingAccountId. Balances are available via this API only for May 1, 2014 or later.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-03-31.
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param billing_period_name: Billing Period Name.
    :type billing_period_name: str

    """
    return web.Response(status=200)
