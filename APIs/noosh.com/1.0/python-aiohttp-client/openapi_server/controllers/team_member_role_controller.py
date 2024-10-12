from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.role_list_vo import RoleListVO
from openapi_server import util


async def get_member_roles(request: web.Request, workgroup_id, project_id, user_id) -> web.Response:
    """List all the role options for the user

    List all the role options for the user

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
