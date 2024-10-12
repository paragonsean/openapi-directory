from typing import List, Dict
from aiohttp import web

from openapi_server.models.barcode_generator_post400_response import BarcodeGeneratorPost400Response
from openapi_server.models.html_renderer_post_request import HtmlRendererPostRequest
from openapi_server import util


async def html_renderer_post(request: web.Request, body) -> web.Response:
    """html_renderer_post

    Generate high-quality PDF documents or images from HTML

    :param body: 
    :type body: dict | bytes

    """
    body = HtmlRendererPostRequest.from_dict(body)
    return web.Response(status=200)
