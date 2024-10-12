from typing import List, Dict
from aiohttp import web

from openapi_server.models.usagenotification_request import UsagenotificationRequest
from openapi_server import util


async def usagenotification(request: web.Request, content_type, accept, body) -> web.Response:
    """Usage notification

    Usage notification

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UsagenotificationRequest.from_dict(body)
    return web.Response(status=200)
