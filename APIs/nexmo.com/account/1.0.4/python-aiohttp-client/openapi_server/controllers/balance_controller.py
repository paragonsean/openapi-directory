from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_balance import AccountBalance
from openapi_server.models.error_authentication_failed_account_balance import ErrorAuthenticationFailedAccountBalance
from openapi_server.models.success import Success
from openapi_server.models.top_up_account_balance401_response import TopUpAccountBalance401Response
from openapi_server import util


async def get_account_balance(request: web.Request, api_key, api_secret) -> web.Response:
    """Get Account Balance

    Retrieve the current balance of your Vonage API account

    :param api_key: Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_secret: str

    """
    return web.Response(status=200)


async def top_up_account_balance(request: web.Request, api_key, api_secret, trx) -> web.Response:
    """Top Up Account Balance

    You can top up your account using this API when you have enabled auto-reload in the dashboard. The amount added by the top-up operation will be the same amount as was added in the payment when auto-reload was enabled. Your account balance is checked every 5-10 minutes and if it falls below the threshold and auto-reload is enabled, then it will be topped up automatically. Use this endpoint  if you need to top up at times when your credit may be exhausted more quickly than the auto-reload may occur.

    :param api_key: Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param trx: The transaction reference of the transaction when balance was added and auto-reload was enabled on your account.
    :type trx: str

    """
    return web.Response(status=200)
