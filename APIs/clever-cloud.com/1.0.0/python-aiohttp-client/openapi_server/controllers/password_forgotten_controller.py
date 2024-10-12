from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_password_forgotten_0(request: web.Request, ) -> web.Response:
    """get_password_forgotten_0

    


    """
    return web.Response(status=200)


async def get_password_forgotten_key_0(request: web.Request, key) -> web.Response:
    """get_password_forgotten_key_0

    

    :param key: 
    :type key: str

    """
    return web.Response(status=200)


async def post_password_forgotten_0(request: web.Request, login=None, drop_tokens=None, tester_pass=None) -> web.Response:
    """post_password_forgotten_0

    

    :param login: 
    :type login: str
    :param drop_tokens: 
    :type drop_tokens: str
    :param tester_pass: 
    :type tester_pass: str

    """
    return web.Response(status=200)


async def post_password_forgotten_key_0(request: web.Request, key, _pass=None, pass2=None) -> web.Response:
    """post_password_forgotten_key_0

    

    :param key: 
    :type key: str
    :param _pass: 
    :type _pass: str
    :param pass2: 
    :type pass2: str

    """
    return web.Response(status=200)
