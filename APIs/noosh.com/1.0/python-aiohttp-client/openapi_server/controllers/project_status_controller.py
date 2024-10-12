from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_status_list_vo import ProjectStatusListVO
from openapi_server import util


async def get_project_status(request: web.Request, workgroup_id) -> web.Response:
    """List the project status

    List the project status

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_project_status_of_client(request: web.Request, workgroup_id, client_workgroup_id) -> web.Response:
    """List the project status of client

    List the project status of client

    :param workgroup_id: 
    :type workgroup_id: str
    :param client_workgroup_id: 
    :type client_workgroup_id: str

    """
    return web.Response(status=200)
