from typing import List, Dict
from aiohttp import web

from openapi_server.models.project import Project
from openapi_server.models.project_request import ProjectRequest
from openapi_server.models.project_response import ProjectResponse
from openapi_server import util


async def projects_create(request: web.Request, body) -> web.Response:
    """Create a new project.

    This POST-Method creates a new project.

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectRequest.from_dict(body)
    return web.Response(status=200)


async def projects_list(request: web.Request, ) -> web.Response:
    """Get user project list.

    This GET-Method lists the user&#39;s projects.


    """
    return web.Response(status=200)


async def projects_read(request: web.Request, project_number) -> web.Response:
    """Get project details.

    This GET-Method returns a specific project.

    :param project_number: Number of the project.
    :type project_number: str

    """
    return web.Response(status=200)
