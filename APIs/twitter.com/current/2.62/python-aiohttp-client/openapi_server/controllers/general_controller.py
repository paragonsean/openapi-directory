from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_open_api_spec(request: web.Request, ) -> web.Response:
    """Returns the OpenAPI Specification document.

    Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)


    """
    return web.Response(status=200)
