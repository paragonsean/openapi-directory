from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_request163_wrapper import NotificationRequest163Wrapper
from openapi_server.models.notification_response166_wrapper import NotificationResponse166Wrapper
from openapi_server import util


async def send_notification_refund_retry(request: web.Request, partner_id, notification_request=None) -> web.Response:
    """Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

    Client can simulate a Mastercard Merchant Presented QR Refund notification to the registered URL endpoint. 

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param notification_request: Contains the details of the request message.
    :type notification_request: dict | bytes

    """
    notification_request = NotificationRequest163Wrapper.from_dict(notification_request)
    return web.Response(status=200)
