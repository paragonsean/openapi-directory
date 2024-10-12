from typing import List, Dict
from aiohttp import web

from openapi_server.models.branch_model import BranchModel
from openapi_server.models.branch_model_results import BranchModelResults
from openapi_server import util


async def v2_tier1_short_name_branch_branches_branch_idget(request: web.Request, short_name, branch_id) -> web.Response:
    """Get a specific branch given its unique Object ID (OID)

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param branch_id: The unique ID of the Branch
    :type branch_id: str

    """
    return web.Response(status=200)


async def v2_tier1_short_name_branch_branches_get(request: web.Request, short_name, offset, count) -> web.Response:
    """All branches defined for a company

    

    :param short_name: The unique client short-name
    :type short_name: str
    :param offset: The index of the first item to return
    :type offset: int
    :param count: The maximum number of items to return (up to 1000 per request)
    :type count: int

    """
    return web.Response(status=200)
