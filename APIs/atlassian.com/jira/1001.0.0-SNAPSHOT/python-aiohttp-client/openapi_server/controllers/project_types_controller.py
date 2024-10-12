from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_type import ProjectType
from openapi_server import util


async def get_accessible_project_type_by_key(request: web.Request, project_type_key) -> web.Response:
    """Get accessible project type by key

    Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param project_type_key: The key of the project type.
    :type project_type_key: str

    """
    return web.Response(status=200)


async def get_all_accessible_project_types(request: web.Request, ) -> web.Response:
    """Get licensed project types

    Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.


    """
    return web.Response(status=200)


async def get_all_project_types(request: web.Request, ) -> web.Response:
    """Get all project types

    Returns all [project types](https://confluence.atlassian.com/x/Var1Nw), whether or not the instance has a valid license for each type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)


async def get_project_type_by_key(request: web.Request, project_type_key) -> web.Response:
    """Get project type by key

    Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.

    :param project_type_key: The key of the project type.
    :type project_type_key: str

    """
    return web.Response(status=200)
