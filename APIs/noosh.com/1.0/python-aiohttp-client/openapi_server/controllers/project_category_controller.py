from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_category_list_vo import ProjectCategoryListVO
from openapi_server import util


async def get_project_category_list(request: web.Request, workgroup_id) -> web.Response:
    """List the project categories

    List the project categories

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_project_category_list_of_client(request: web.Request, workgroup_id, client_workgroup_id) -> web.Response:
    """List the project categories of client side

    List the project categories of client side

    :param workgroup_id: 
    :type workgroup_id: str
    :param client_workgroup_id: 
    :type client_workgroup_id: str

    """
    return web.Response(status=200)
