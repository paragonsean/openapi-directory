from typing import List, Dict
from aiohttp import web

from openapi_server.models.markdown_render_request import MarkdownRenderRequest
from openapi_server import util


async def markdown_render(request: web.Request, body) -> web.Response:
    """Render a Markdown document

    

    :param body: 
    :type body: dict | bytes

    """
    body = MarkdownRenderRequest.from_dict(body)
    return web.Response(status=200)


async def markdown_render_raw(request: web.Request, body=None) -> web.Response:
    """Render a Markdown document in raw mode

    You must send Markdown as plain text (using a &#x60;Content-Type&#x60; header of &#x60;text/plain&#x60; or &#x60;text/x-markdown&#x60;) to this endpoint, rather than using JSON format. In raw mode, [GitHub Flavored Markdown](https://github.github.com/gfm/) is not supported and Markdown will be rendered in plain format like a README.md file. Markdown content must be 400 KB or less.

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
