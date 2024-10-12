from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def jsontoxml_post(request: web.Request, body) -> web.Response:
    """jsontoxml_post

    

    :param body: JSON payload
    :type body: str

    """
    return web.Response(status=200)


async def xmltojson_post(request: web.Request, body) -> web.Response:
    """xmltojson_post

    

    :param body: XML payload
    :type body: str

    """
    return web.Response(status=200)
