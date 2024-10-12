from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def password_generate(request: web.Request, length, upper_case=None, digits=None, special_characters=None) -> web.Response:
    """password_generate

    

    :param length: 
    :type length: int
    :param upper_case: 
    :type upper_case: bool
    :param digits: 
    :type digits: bool
    :param special_characters: 
    :type special_characters: bool

    """
    return web.Response(status=200)


async def password_validate(request: web.Request, password) -> web.Response:
    """password_validate

    

    :param password: 
    :type password: str

    """
    return web.Response(status=200)
