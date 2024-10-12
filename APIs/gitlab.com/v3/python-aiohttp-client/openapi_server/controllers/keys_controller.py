from typing import List, Dict
from aiohttp import web

from openapi_server.models.ssh_key_with_user import SSHKeyWithUser
from openapi_server import util


async def get_v3_keys_id(request: web.Request, id) -> web.Response:
    """Get single ssh key by id. Only available to admin users

    Get single ssh key by id. Only available to admin users

    :param id: 
    :type id: int

    """
    return web.Response(status=200)
