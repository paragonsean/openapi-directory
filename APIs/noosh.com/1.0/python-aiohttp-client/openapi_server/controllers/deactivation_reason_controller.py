from typing import List, Dict
from aiohttp import web

from openapi_server.models.deactivation_reason_list_vo import DeactivationReasonListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server import util


async def get_deactivation_reason_list(request: web.Request, workgroup_id) -> web.Response:
    """List all deactivation reasons

    List all deactivation reasons

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
