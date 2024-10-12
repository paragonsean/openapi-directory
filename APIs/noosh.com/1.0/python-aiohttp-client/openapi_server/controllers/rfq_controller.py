from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.rfq_expand_vo import RfqExpandVO
from openapi_server.models.rfq_list_vo import RfqListVO
from openapi_server import util


async def get_rfq(request: web.Request, workgroup_id, project_id, rfq_id) -> web.Response:
    """Get a specific Rfq

    Get a specific Rfq

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param rfq_id: 
    :type rfq_id: str

    """
    return web.Response(status=200)


async def get_rfq_list(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List the rfqs

    List the rfqs

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)
