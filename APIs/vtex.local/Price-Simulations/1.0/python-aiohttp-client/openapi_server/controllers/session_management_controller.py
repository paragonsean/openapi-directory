from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server import util


async def sessions_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Update Order Configuration

    Updates the Order Configuration. You should use this route every time you edit a configuration value

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody.from_dict(body)
    return web.Response(status=200)
