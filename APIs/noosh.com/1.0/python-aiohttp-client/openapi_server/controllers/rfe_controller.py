from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.rfe_expand_vo import RfeExpandVO
from openapi_server.models.rfe_list_vo import RfeListVO
from openapi_server.models.rfe_po import RfePO
from openapi_server.models.rfq_vo import RfqVO
from openapi_server import util


async def get_rfe(request: web.Request, workgroup_id, project_id, rfe_id) -> web.Response:
    """Get a specific Rfe

    Get a specific Rfe

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param rfe_id: 
    :type rfe_id: str

    """
    return web.Response(status=200)


async def get_rfe_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List the RFES

    List the RFES

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def post_rfe(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Create a RFE

    Create a RFE

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RfePO.from_dict(body)
    return web.Response(status=200)
