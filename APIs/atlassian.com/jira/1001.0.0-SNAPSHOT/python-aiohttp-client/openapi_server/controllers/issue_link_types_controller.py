from typing import List, Dict
from aiohttp import web

from openapi_server.models.issue_link_type import IssueLinkType
from openapi_server.models.issue_link_types import IssueLinkTypes
from openapi_server import util


async def create_issue_link_type(request: web.Request, body) -> web.Response:
    """Create issue link type

    Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link&#39;s inward and outward relationships.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: 
    :type body: dict | bytes

    """
    body = IssueLinkType.from_dict(body)
    return web.Response(status=200)


async def delete_issue_link_type(request: web.Request, issue_link_type_id) -> web.Response:
    """Delete issue link type

    Deletes an issue link type.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_link_type_id: The ID of the issue link type.
    :type issue_link_type_id: str

    """
    return web.Response(status=200)


async def get_issue_link_type(request: web.Request, issue_link_type_id) -> web.Response:
    """Get issue link type

    Returns an issue link type.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

    :param issue_link_type_id: The ID of the issue link type.
    :type issue_link_type_id: str

    """
    return web.Response(status=200)


async def get_issue_link_types(request: web.Request, ) -> web.Response:
    """Get issue link types

    Returns a list of all issue link types.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.


    """
    return web.Response(status=200)


async def update_issue_link_type(request: web.Request, issue_link_type_id, body) -> web.Response:
    """Update issue link type

    Updates an issue link type.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param issue_link_type_id: The ID of the issue link type.
    :type issue_link_type_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = IssueLinkType.from_dict(body)
    return web.Response(status=200)
