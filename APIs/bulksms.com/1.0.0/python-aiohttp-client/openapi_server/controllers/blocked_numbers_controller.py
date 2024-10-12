from typing import List, Dict
from aiohttp import web

from openapi_server.models.blocked_number import BlockedNumber
from openapi_server import util


async def blocked_numbers_get(request: web.Request, min_id=None, limit=None) -> web.Response:
    """List blocked numbers

    

    :param min_id: Records with an &#x60;id&#x60; that is greater or equal to min-id will be returned. The default value is &#x60;0&#x60;.  You can add 1 to an id that you previously retrieved, to return subsequent records.
    :type min_id: int
    :param limit: The maximum number of records to return. The default value is &#x60;10000&#x60;. The value cannot be greater than 10000.
    :type limit: int

    """
    return web.Response(status=200)


async def blocked_numbers_post(request: web.Request, body) -> web.Response:
    """Create a blocked number

    Blocked numbers are phone numbers to which your account is not permitted to send messages. The numbers can be created via this API, by a recipient replying with a STOP message to one of your previous SENT messages, or by a BulkSMS administrator.  Sending a message to a blocked number will result in the message being assigned a status of &#x60;FAILED.BLOCKED&#x60;. Messages sent to blocked numbers are billed to your account. 

    :param body: Maximum size: &#x60;1000&#x60; items
    :type body: List[str]

    """
    return web.Response(status=200)
