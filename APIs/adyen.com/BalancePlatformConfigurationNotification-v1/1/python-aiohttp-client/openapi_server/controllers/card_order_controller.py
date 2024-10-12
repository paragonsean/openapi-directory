from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.card_order_notification_request import CardOrderNotificationRequest
from openapi_server import util


async def post_balance_platform_cardorder_created(request: web.Request, card_order_notification_request=None) -> web.Response:
    """Card order created

    Adyen sends this webhook to indicate a successful creation of a card order after you create a [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments) of &#x60;type&#x60; **card** and &#x60;formFactor&#x60; **physical**.

    :param card_order_notification_request: 
    :type card_order_notification_request: dict | bytes

    """
    card_order_notification_request = CardOrderNotificationRequest.from_dict(card_order_notification_request)
    return web.Response(status=200)


async def post_balance_platform_cardorder_updated(request: web.Request, card_order_notification_request=None) -> web.Response:
    """Card order updated

    Adyen sends this webhook when there is an update in card order status.

    :param card_order_notification_request: 
    :type card_order_notification_request: dict | bytes

    """
    card_order_notification_request = CardOrderNotificationRequest.from_dict(card_order_notification_request)
    return web.Response(status=200)
