from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def request_api_key(request: web.Request, api_key_l1, api_key_l2, email, password, user_first_name, user_last_name) -> web.Response:
    """requestApiKey

    

    :param api_key_l1: Api Key for client
    :type api_key_l1: str
    :param api_key_l2: Integration Partner Api Key
    :type api_key_l2: str
    :param email: User email
    :type email: str
    :param password: User password
    :type password: int
    :param user_first_name: User first name
    :type user_first_name: str
    :param user_last_name: User last name
    :type user_last_name: str

    """
    return web.Response(status=200)
