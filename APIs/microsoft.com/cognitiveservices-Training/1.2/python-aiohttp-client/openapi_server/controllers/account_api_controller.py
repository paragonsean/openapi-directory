from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server import util


async def get_account_info(request: web.Request, training_key) -> web.Response:
    """Get basic information about your account

    

    :param training_key: 
    :type training_key: str

    """
    return web.Response(status=200)
