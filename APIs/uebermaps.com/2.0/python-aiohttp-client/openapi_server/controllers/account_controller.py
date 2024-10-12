from typing import List, Dict
from aiohttp import web

from openapi_server.models.user import User
from openapi_server.models.user_editable import UserEditable
from openapi_server import util


async def account_patch(request: web.Request, user=None) -> web.Response:
    """Update account

    Update account. Wrap map parameters in [user].

    :param user: user attributes
    :type user: dict | bytes

    """
    user = UserEditable.from_dict(user)
    return web.Response(status=200)
