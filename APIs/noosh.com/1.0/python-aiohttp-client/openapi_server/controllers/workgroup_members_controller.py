from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.user_details_expand_vo import UserDetailsExpandVO
from openapi_server.models.workgroup_members_list_vo import WorkgroupMembersListVO
from openapi_server import util


async def get_workgroup_member_info(request: web.Request, workgroup_id, user_id) -> web.Response:
    """Workgroup Member Info

    Workgroup Member Info

    :param workgroup_id: 
    :type workgroup_id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_workgroup_member_list(request: web.Request, workgroup_id) -> web.Response:
    """List the workgroup members

    List the workgroup members

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
