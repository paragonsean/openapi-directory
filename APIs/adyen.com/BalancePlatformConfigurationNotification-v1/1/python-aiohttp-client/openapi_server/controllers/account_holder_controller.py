from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_holder_notification_request import AccountHolderNotificationRequest
from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server import util


async def post_balance_platform_account_holder_created(request: web.Request, account_holder_notification_request=None) -> web.Response:
    """Account holder created

    Adyen sends this webhook when you successfully [create an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/accountHolders).

    :param account_holder_notification_request: 
    :type account_holder_notification_request: dict | bytes

    """
    account_holder_notification_request = AccountHolderNotificationRequest.from_dict(account_holder_notification_request)
    return web.Response(status=200)


async def post_balance_platform_account_holder_updated(request: web.Request, account_holder_notification_request=None) -> web.Response:
    """Account holder updated

    Adyen sends this webhook when you successfully [update an account holder](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/accountHolders/_id_).

    :param account_holder_notification_request: 
    :type account_holder_notification_request: dict | bytes

    """
    account_holder_notification_request = AccountHolderNotificationRequest.from_dict(account_holder_notification_request)
    return web.Response(status=200)
