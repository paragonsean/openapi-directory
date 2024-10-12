from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def voice(request: web.Request, to, text, xml=None, _from=None) -> web.Response:
    """voice

    

    :param to: Determines the receiver. Must be a valid phone number or contact from the address book.
    :type to: str
    :param text: The text to convert to a voice message. Accepts valid XML too.
    :type text: str
    :param xml: Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0.
    :type xml: 
    :param _from: Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours.
    :type _from: str

    """
    return web.Response(status=200)
