from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def convert(request: web.Request, filename=None, source=None, validate=None) -> web.Response:
    """Convert a Swagger 2.0 definition passed in the body to OpenAPI 3.0.x 

    

    :param filename: The file to upload and convert
    :type filename: str
    :param source: The text of a Swagger 2.0 definition to convert
    :type source: str
    :param validate: 
    :type validate: str

    """
    return web.Response(status=200)


async def convert_url(request: web.Request, url) -> web.Response:
    """Convert a Swagger 2.0 definition to OpenAPI 3.0.x from a URL

    

    :param url: The URL to retrieve the OpenAPI 2.0 definition from
    :type url: str

    """
    return web.Response(status=200)
