from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_category import ProjectCategory
from openapi_server.models.updated_project_category import UpdatedProjectCategory
from openapi_server import util


async def create_project_category(request: web.Request, body) -> web.Response:
    """Create project category

    Creates a project category.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = ProjectCategory.from_dict(body)
    return web.Response(status=200)


async def get_all_project_categories(request: web.Request, ) -> web.Response:
    """Get all project categories

    Returns all project categories.  **[Permissions](#permissions) required:** Permission to access Jira.


    """
    return web.Response(status=200)


async def get_project_category_by_id(request: web.Request, id) -> web.Response:
    """Get project category by ID

    Returns a project category.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param id: The ID of the project category.
    :type id: int

    """
    return web.Response(status=200)


async def remove_project_category(request: web.Request, id) -> web.Response:
    """Delete project category

    Deletes a project category.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: ID of the project category to delete.
    :type id: int

    """
    return web.Response(status=200)


async def update_project_category(request: web.Request, id, body) -> web.Response:
    """Update project category

    Updates a project category.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProjectCategory.from_dict(body)
    return web.Response(status=200)
