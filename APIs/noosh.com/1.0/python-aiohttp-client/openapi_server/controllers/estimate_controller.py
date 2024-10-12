from typing import List, Dict
from aiohttp import web

from openapi_server.models.estimate_expand_vo import EstimateExpandVO
from openapi_server.models.estimate_list_expand_vo import EstimateListExpandVO
from openapi_server.models.estimate_po import EstimatePO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server import util


async def get_estimate(request: web.Request, workgroup_id, project_id, estimate_id) -> web.Response:
    """Get a specific estimate of project

    Get a specific estimate of project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param estimate_id: 
    :type estimate_id: str

    """
    return web.Response(status=200)


async def get_estimate_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List the Estimates

    List the Estimates

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def post_estimate(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a Estimate

    Create a Estimate

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = EstimatePO.from_dict(body)
    return web.Response(status=200)
