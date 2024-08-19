from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.redirect_response import RedirectResponse
from openapi_server.models.render_request import RenderRequest
from openapi_server.models.render_response import RenderResponse
from openapi_server import util


async def render_sync(request: web.Request, body) -> web.Response:
    """Render a URL as an image or video

    

    :param body: 
    :type body: dict | bytes

    """
    body = RenderRequest.from_dict(body)
    return web.Response(status=200)
