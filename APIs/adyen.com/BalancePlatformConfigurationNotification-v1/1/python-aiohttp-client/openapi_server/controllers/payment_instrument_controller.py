from typing import List, Dict
from aiohttp import web

from openapi_server.models.balance_platform_notification_response import BalancePlatformNotificationResponse
from openapi_server.models.payment_notification_request import PaymentNotificationRequest
from openapi_server import util


async def post_balance_platform_payment_instrument_created(request: web.Request, payment_notification_request=None) -> web.Response:
    """Payment instrument created

    Adyen sends this webhook when you successfully [create a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments).  &gt;The webhook does not include the card number when creating virtual cards. You can only get the card number in the response of the POST [/paymentInstruments](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/paymentInstruments#responses-200-card-number) request.

    :param payment_notification_request: 
    :type payment_notification_request: dict | bytes

    """
    payment_notification_request = PaymentNotificationRequest.from_dict(payment_notification_request)
    return web.Response(status=200)


async def post_balance_platform_payment_instrument_updated(request: web.Request, payment_notification_request=None) -> web.Response:
    """Payment instrument updated

    Adyen sends this webhook when you successfully [update a payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/patch/paymentInstruments/_id_). 

    :param payment_notification_request: 
    :type payment_notification_request: dict | bytes

    """
    payment_notification_request = PaymentNotificationRequest.from_dict(payment_notification_request)
    return web.Response(status=200)
