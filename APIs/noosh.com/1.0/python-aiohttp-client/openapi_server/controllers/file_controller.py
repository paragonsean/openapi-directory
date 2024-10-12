from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_response_vo import FileResponseVO
from openapi_server.models.file_tag_response_vo import FileTagResponseVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server import util


async def get_file(request: web.Request, workgroup_id, project_id, file_id) -> web.Response:
    """Get File from Project.  Works for Regular and Remote Files

    Get File from Project.  Works for Regular and Remote Files

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param file_id: 
    :type file_id: str

    """
    return web.Response(status=200)


async def get_file_tags(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List Tags from Workgroup and Project.

    List Tags from Workgroup and Project.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_files(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List Files from Project.  Works for Regular and Remote Files

    List Files from Project.  Works for Regular and Remote Files

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def upload_file(request: web.Request, workgroup_id, project_id) -> web.Response:
    """Upload File to Project.  A multipart/form-data request with a name \&quot;file\&quot;

    Upload File to Project.  A multipart/form-data request with a name \&quot;file\&quot;

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)
