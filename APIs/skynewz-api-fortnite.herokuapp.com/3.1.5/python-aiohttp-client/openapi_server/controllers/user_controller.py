from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_get_default_response import CheckGetDefaultResponse
from openapi_server.models.user_plateform_username_get200_response import UserPlateformUsernameGet200Response
from openapi_server import util


async def user_plateform_username_get(request: web.Request, plateform, username) -> web.Response:
    """Get a user by username

    

    :param plateform: Playing plateform, can be xb1, ps4 or pc
    :type plateform: str
    :param username: Player username
    :type username: str

    """
    return web.Response(status=200)
