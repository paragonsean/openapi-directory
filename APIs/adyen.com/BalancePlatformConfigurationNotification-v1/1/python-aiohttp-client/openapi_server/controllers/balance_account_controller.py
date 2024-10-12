from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_account_notification_request import BalanceAccountNotificationRequest
from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.sweep_configuration_notification_request import SweepConfigurationNotificationRequest
from openapi_server import util


async def post_balance_platform_balance_account_created(request: web.Request, balance_account_notification_request=None) -> web.Response:
    """Balance account created

    Adyen sends this webhook when you successfully [create a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts).

    :param balance_account_notification_request: 
    :type balance_account_notification_request: dict | bytes

    """
    balance_account_notification_request = BalanceAccountNotificationRequest.from_dict(balance_account_notification_request)
    return web.Response(status=200)


async def post_balance_platform_balance_account_sweep_created(request: web.Request, sweep_configuration_notification_request=None) -> web.Response:
    """Sweep created

    Adyen sends this webhook when you successfully [create a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts/_balanceAccountId_/sweeps).

    :param sweep_configuration_notification_request: 
    :type sweep_configuration_notification_request: dict | bytes

    """
    sweep_configuration_notification_request = SweepConfigurationNotificationRequest.from_dict(sweep_configuration_notification_request)
    return web.Response(status=200)


async def post_balance_platform_balance_account_sweep_deleted(request: web.Request, sweep_configuration_notification_request=None) -> web.Response:
    """Sweep deleted

    Adyen sends this webhook when you successfully [delete a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/delete/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

    :param sweep_configuration_notification_request: 
    :type sweep_configuration_notification_request: dict | bytes

    """
    sweep_configuration_notification_request = SweepConfigurationNotificationRequest.from_dict(sweep_configuration_notification_request)
    return web.Response(status=200)


async def post_balance_platform_balance_account_sweep_updated(request: web.Request, sweep_configuration_notification_request=None) -> web.Response:
    """Sweep updated

    Adyen sends this webhook when you successfully [update a sweep](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_balanceAccountId_/sweeps/_sweepId_).

    :param sweep_configuration_notification_request: 
    :type sweep_configuration_notification_request: dict | bytes

    """
    sweep_configuration_notification_request = SweepConfigurationNotificationRequest.from_dict(sweep_configuration_notification_request)
    return web.Response(status=200)


async def post_balance_platform_balance_account_updated(request: web.Request, balance_account_notification_request=None) -> web.Response:
    """Balance account updated

    Adyen sends this webhook when you successfully [update a balance account](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/balanceAccounts/_id_).

    :param balance_account_notification_request: 
    :type balance_account_notification_request: dict | bytes

    """
    balance_account_notification_request = BalanceAccountNotificationRequest.from_dict(balance_account_notification_request)
    return web.Response(status=200)
