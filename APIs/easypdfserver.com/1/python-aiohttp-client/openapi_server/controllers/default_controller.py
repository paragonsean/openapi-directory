from typing import List, Dict
from aiohttp import web

from openapi_server.models.make_pdf_post_request import MakePdfPostRequest
from openapi_server import util


async def make_pdf_post(request: web.Request, body) -> web.Response:
    """Generate a PDF from HTML or URL.

    

    :param body: Pass the API key from easypdfserver.com and either HTML or URL to generate your PDF.
    :type body: dict | bytes

    """
    body = MakePdfPostRequest.from_dict(body)
    return web.Response(status=200)
