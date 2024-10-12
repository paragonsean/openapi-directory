from typing import List, Dict
from aiohttp import web

from openapi_server.models.notification_result_object import NotificationResultObject
from openapi_server import util


async def notify_result(request: web.Request, request_id, notifcation_result=None) -> web.Response:
    """Push Notification Payload

    Whenever you request that a transaction be put into the background, there needs to be a mechanism for notifying you that the request has been completed. This notification will push you the high-level details of the result, and you can then query the results at your leisiure.  The same notification process will also be used to push alerts to your system. This means that RequestIDs may not match your records 

    :param request_id: This will be the same RequestId that was sent in the 202 acceptance response. 
    :type request_id: str
    :param notifcation_result: 
    :type notifcation_result: dict | bytes

    """
    notifcation_result = NotificationResultObject.from_dict(notifcation_result)
    return web.Response(status=200)
