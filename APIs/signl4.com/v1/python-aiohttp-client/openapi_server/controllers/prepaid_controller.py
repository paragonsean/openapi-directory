from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.prepaid_balance_info import PrepaidBalanceInfo
from openapi_server.models.prepaid_settings_info import PrepaidSettingsInfo
from openapi_server.models.prepaid_transaction_info import PrepaidTransactionInfo
from openapi_server import util


async def prepaid_balance_get(request: web.Request, ) -> web.Response:
    """Get your subscription&#39;s current prepaid balance.

    


    """
    return web.Response(status=200)


async def prepaid_settings_get(request: web.Request, ) -> web.Response:
    """Get your subscription&#39;s current prepaid settings.

    


    """
    return web.Response(status=200)


async def prepaid_settings_put(request: web.Request, body=None) -> web.Response:
    """Update your subscription&#39;s current prepaid settings.

    

    :param body: Settings object containing the new values.
    :type body: dict | bytes

    """
    body = PrepaidSettingsInfo.from_dict(body)
    return web.Response(status=200)


async def prepaid_transactions_get(request: web.Request, ) -> web.Response:
    """Get your subscription&#39;s prepaid transactions.

    


    """
    return web.Response(status=200)


async def subscriptions_subscription_id_prepaid_balance_get(request: web.Request, subscription_id) -> web.Response:
    """Get a subscription&#39;s current prepaid balance.

    

    :param subscription_id: 
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_subscription_id_prepaid_settings_get(request: web.Request, subscription_id) -> web.Response:
    """Get a subscription&#39;s current prepaid settings.

    

    :param subscription_id: 
    :type subscription_id: str

    """
    return web.Response(status=200)


async def subscriptions_subscription_id_prepaid_settings_put(request: web.Request, subscription_id, body=None) -> web.Response:
    """Update a subscription&#39;s current prepaid settings.

    

    :param subscription_id: ID of the subscription
    :type subscription_id: str
    :param body: Settings object containing the new values.
    :type body: dict | bytes

    """
    body = PrepaidSettingsInfo.from_dict(body)
    return web.Response(status=200)


async def subscriptions_subscription_id_prepaid_transactions_get(request: web.Request, subscription_id) -> web.Response:
    """Get a subscription&#39;s prepaid transactions.

    

    :param subscription_id: ID of the subscription to get transactions for
    :type subscription_id: str

    """
    return web.Response(status=200)
