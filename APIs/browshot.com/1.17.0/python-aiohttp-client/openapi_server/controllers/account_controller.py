from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_error import AccountError
from openapi_server import util


async def get_account_info(request: web.Request, details=None) -> web.Response:
    """Get information about your account

    Get information about your account.

    :param details: level of information returned
    :type details: int

    """
    return web.Response(status=200)
