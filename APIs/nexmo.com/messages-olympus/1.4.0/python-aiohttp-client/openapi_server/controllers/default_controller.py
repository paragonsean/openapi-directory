from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_internal import ErrorInternal
from openapi_server.models.error_payment_required import ErrorPaymentRequired
from openapi_server.models.error_throttled import ErrorThrottled
from openapi_server.models.send_message202_response import SendMessage202Response
from openapi_server.models.send_message401_response import SendMessage401Response
from openapi_server.models.send_message422_response import SendMessage422Response
from openapi_server.models.send_message_request import SendMessageRequest
from openapi_server import util


async def send_message(request: web.Request, body) -> web.Response:
    """Send a message to the given channel.

    Send a Message

    :param body: Send a Message.
    :type body: dict | bytes

    """
    body = SendMessageRequest.from_dict(body)
    return web.Response(status=200)
