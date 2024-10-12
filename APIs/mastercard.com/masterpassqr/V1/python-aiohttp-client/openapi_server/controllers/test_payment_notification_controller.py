from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_request159_wrapper import NotificationRequest159Wrapper
from openapi_server.models.notification_response162_wrapper import NotificationResponse162Wrapper
from openapi_server import util


async def send_notification_payment_retry(request: web.Request, partner_id, notification_request=None) -> web.Response:
    """Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

    Client can simulate a Mastercard Merchant Presented QR Payment notification to the registered URL endpoint. 

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param notification_request: Contains the details of the request message.
    :type notification_request: dict | bytes

    """
    notification_request = NotificationRequest159Wrapper.from_dict(notification_request)
    return web.Response(status=200)
