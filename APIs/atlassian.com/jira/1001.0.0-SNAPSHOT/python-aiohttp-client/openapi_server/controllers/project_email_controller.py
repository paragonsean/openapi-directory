from typing import List, Dict
from aiohttp import web

from openapi_server.models.project_email_address import ProjectEmailAddress
from openapi_server import util


async def get_project_email(request: web.Request, project_id) -> web.Response:
    """Get project&#39;s sender email

    Returns the [project&#39;s sender email address](https://confluence.atlassian.com/x/dolKLg).  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id: The project ID.
    :type project_id: int

    """
    return web.Response(status=200)


async def update_project_email(request: web.Request, project_id, body) -> web.Response:
    """Set project&#39;s sender email

    Sets the [project&#39;s sender email address](https://confluence.atlassian.com/x/dolKLg).  If &#x60;emailAddress&#x60; is an empty string, the default email address is restored.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    :param project_id: The project ID.
    :type project_id: int
    :param body: The project&#39;s sender email address to be set.
    :type body: dict | bytes

    """
    body = ProjectEmailAddress.from_dict(body)
    return web.Response(status=200)
