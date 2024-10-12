from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body1 import RequestBody1
from openapi_server import util


async def v_custom_prices_session_schema_get(request: web.Request, content_type, accept) -> web.Response:
    """Get custom prices schema

    Retrieves all custom price for all shopping scenarios

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def v_custom_prices_session_schema_post(request: web.Request, content_type, accept, body=None) -> web.Response:
    """Create or Update custom prices schema

    Creates a new custom price for a shopping scenario or updates an existing one

    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody1.from_dict(body)
    return web.Response(status=200)
