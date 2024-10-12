from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_role import ApplicationRole
from openapi_server import util


async def get_all_application_roles(request: web.Request, ) -> web.Response:
    """Get all application roles

    Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).


    """
    return web.Response(status=200)


async def get_application_role(request: web.Request, key) -> web.Response:
    """Get application role

    Returns an application role.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param key: The key of the application role. Use the [Get all application roles](#api-rest-api-3-applicationrole-get) operation to get the key for each application role.
    :type key: str

    """
    return web.Response(status=200)
