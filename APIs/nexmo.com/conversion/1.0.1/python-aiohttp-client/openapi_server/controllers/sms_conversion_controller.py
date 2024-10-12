from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def sms_conversion(request: web.Request, message_id, delivered, timestamp) -> web.Response:
    """Tell Nexmo if your SMS message was successful

    Send a Conversion API request with information about the SMS message identified by &#x60;message-id&#x60;. Nexmo uses your conversion data and internal information about &#x60;message-id&#x60; to help improve our routing of messages in the future.

    :param message_id: The ID you receive in the response to a request. * From the Verify API - use the &#x60;event_id&#x60; in the response to Verify Check. * From the SMS API - use the &#x60;message-id&#x60; * From the Text-To-Speech API - use the &#x60;call-id&#x60; * From the Text-To-Speech-Prompt API - use the &#x60;call-id&#x60;
    :type message_id: str
    :param delivered: Set to _true_ if your user replied to the message you sent. Otherwise, set to _false_. **Note**: for curl, use 0 and 1.
    :type delivered: bool
    :param timestamp: When the user completed your call-to-action (e.g. visited your website, installed your app) in [UTC±00:00](https://en.wikipedia.org/wiki/UTC%C2%B100:00) format: _yyyy-MM-dd HH:mm:ss_. If you do not set this parameter, Nexmo uses the time it receives this request.
    :type timestamp: str

    """
    return web.Response(status=200)
