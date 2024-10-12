from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_entity import ProjectEntity
from openapi_server import util


async def delete_projects_id(request: web.Request, id) -> web.Response:
    """Delete Project

    Delete Project

    :param id: Project ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_projects(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List Projects

    List Projects

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_projects_id(request: web.Request, id) -> web.Response:
    """Show Project

    Show Project

    :param id: Project ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_projects_id(request: web.Request, id, global_access) -> web.Response:
    """Update Project

    Update Project

    :param id: Project ID.
    :type id: int
    :param global_access: Global permissions.  Can be: &#x60;none&#x60;, &#x60;anyone_with_read&#x60;, &#x60;anyone_with_full&#x60;.
    :type global_access: str

    """
    return web.Response(status=200)


async def post_projects(request: web.Request, global_access) -> web.Response:
    """Create Project

    Create Project

    :param global_access: Global permissions.  Can be: &#x60;none&#x60;, &#x60;anyone_with_read&#x60;, &#x60;anyone_with_full&#x60;.
    :type global_access: str

    """
    return web.Response(status=200)
