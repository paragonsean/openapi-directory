from typing import List, Dict
from aiohttp import web

from openapi_server.models.sms200_response import Sms200Response
from openapi_server import util


async def sms(request: web.Request, text, to, _from=None, foreign_id=None, label=None, udh=None, delay=None, debug=None, no_reload=None, unicode=None, flash=None, utf8=None, details=None, return_msg_id=None, _json=None, performance_tracking=None) -> web.Response:
    """sms

    

    :param text: The actual text message to send.
    :type text: str
    :param to: The recipient number or group name.
    :type to: str
    :param _from: Set a custom sender name.
    :type _from: str
    :param foreign_id: Identifier to return in callbacks.
    :type foreign_id: str
    :param label: A custom label.
    :type label: str
    :param udh: A custom User Data Header.
    :type udh: str
    :param delay: Date/Time for delayed dispatch.
    :type delay: str
    :param debug: Disable message sending.
    :type debug: 
    :param no_reload: Enable sending of duplicated messages within 180 seconds.
    :type no_reload: 
    :param unicode: Force unicode encoding. Reduces sms length to 70 chars.
    :type unicode: 
    :param flash: Send as flash.
    :type flash: 
    :param utf8: Force UTF8 encoding.
    :type utf8: 
    :param details: Attach message details to response.
    :type details: 
    :param return_msg_id: Attach message ID to second row in a text response.
    :type return_msg_id: 
    :param _json: Return a detailed JSON response.
    :type _json: 
    :param performance_tracking: Enable performance tracking for found URLs.
    :type performance_tracking: 

    """
    return web.Response(status=200)
