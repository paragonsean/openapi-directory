from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_payor_link_request import CreatePayorLinkRequest
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server import util


async def create_payor_links(request: web.Request, body) -> web.Response:
    """Create a Payor Link

    This endpoint allows you to create a payor link.

    :param body: Request to create a payor link
    :type body: dict | bytes

    """
    body = CreatePayorLinkRequest.from_dict(body)
    return web.Response(status=200)
