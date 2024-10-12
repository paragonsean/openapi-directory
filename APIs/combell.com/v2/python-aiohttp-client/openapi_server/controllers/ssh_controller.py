from typing import List, Dict
from aiohttp import web

from openapi_server.models.ssh_key_detail import SshKeyDetail
from openapi_server import util


async def get_all_ssh_keys(request: web.Request, skip=None, take=None) -> web.Response:
    """Overview of SSH keys

    

    :param skip: The number of items to skip in the resultset.
    :type skip: int
    :param take: The number of items to return in the resultset. The returned count can be equal or less than this number.
    :type take: int

    """
    return web.Response(status=200)
