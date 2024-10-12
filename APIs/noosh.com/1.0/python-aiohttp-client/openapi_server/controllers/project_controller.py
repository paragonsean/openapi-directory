from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.project_expand_vo import ProjectExpandVO
from openapi_server.models.project_id_list_vo import ProjectIdListVO
from openapi_server.models.project_list_vo import ProjectListVO
from openapi_server.models.project_patch_po import ProjectPatchPO
from openapi_server.models.project_persist_vo import ProjectPersistVO
from openapi_server.models.project_vo import ProjectVO
from openapi_server import util


async def attach_project(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Attach children projects to specific Project

    Attach children projects to specific Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectIdListVO.from_dict(body)
    return web.Response(status=200)


async def delete_project(request: web.Request, workgroup_id, project_id) -> web.Response:
    """Archieve a specific Project

    Archieve a specific Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_project(request: web.Request, workgroup_id, project_id) -> web.Response:
    """Get a specific Project

    Get a specific Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_project_list(request: web.Request, workgroup_id) -> web.Response:
    """List the projects

    List the projects

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def patch_project(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Patch a specific Project

    Patch a specific Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectPatchPO.from_dict(body)
    return web.Response(status=200)


async def post_project(request: web.Request, workgroup_id, body=None) -> web.Response:
    """Create a Project

    Create a Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectPersistVO.from_dict(body)
    return web.Response(status=200)


async def put_project(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Update a specific Project

    Update a specific Project

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectPersistVO.from_dict(body)
    return web.Response(status=200)
