from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_home_user_fields_list_vo import ProjectHomeUserFieldsListVO
from openapi_server import util


async def get_project_home_user_field_list_of_client(request: web.Request, workgroup_id, client_workgroup_id) -> web.Response:
    """List projec home user fields of client workgroup

    List projec home user fields of client workgroup

    :param workgroup_id: 
    :type workgroup_id: str
    :param client_workgroup_id: 
    :type client_workgroup_id: str

    """
    return web.Response(status=200)


async def get_project_home_user_fields_list(request: web.Request, workgroup_id) -> web.Response:
    """List projec home user fields

    List projec home user fields

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)
