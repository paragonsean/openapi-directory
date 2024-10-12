from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_markdown_emoticons import EndpointGetMarkdownEmoticons
from openapi_server.models.endpoint_post_markdown import EndpointPostMarkdown
from openapi_server import util


async def markdown_emoticons_get(request: web.Request, ) -> web.Response:
    """markdown_emoticons_get

    


    """
    return web.Response(status=200)


async def markdown_post(request: web.Request, text_raw, text_emoticons=None) -> web.Response:
    """markdown_post

    

    :param text_raw: 
    :type text_raw: str
    :param text_emoticons: 
    :type text_emoticons: bool

    """
    return web.Response(status=200)
