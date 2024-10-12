from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def auto_check_in(request: web.Request, ticketnumber, email_address, accept) -> web.Response:
    """Auto Check-In

    Trigger an automatic check-in given a ticket number. This service is only accessible for LH privileged partners

    :param ticketnumber: Ticket number
    :type ticketnumber: str
    :param email_address: Email address
    :type email_address: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str

    """
    return web.Response(status=200)
