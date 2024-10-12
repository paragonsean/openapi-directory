from typing import List, Dict
from aiohttp import web

from openapi_server.models.test_echo import TestEcho
from openapi_server.models.test_validate import TestValidate
from openapi_server import util


async def echo(request: web.Request, text=None) -> web.Response:
    """Echo text

    

    :param text: Text to echo
    :type text: str

    """
    return web.Response(status=200)


async def validate(request: web.Request, id, tag=None, user_agent=None) -> web.Response:
    """Validate input

    

    :param id: Integer ID
    :type id: int
    :param tag: List of tags
    :type tag: List[str]
    :param user_agent: User agent
    :type user_agent: str

    """
    return web.Response(status=200)
