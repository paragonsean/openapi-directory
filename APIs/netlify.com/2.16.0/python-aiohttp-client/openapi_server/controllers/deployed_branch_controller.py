from typing import List, Dict
from aiohttp import web

from openapi_server.models.deployed_branch import DeployedBranch
from openapi_server.models.error import Error
from openapi_server import util


async def list_site_deployed_branches(request: web.Request, site_id) -> web.Response:
    """list_site_deployed_branches

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)
