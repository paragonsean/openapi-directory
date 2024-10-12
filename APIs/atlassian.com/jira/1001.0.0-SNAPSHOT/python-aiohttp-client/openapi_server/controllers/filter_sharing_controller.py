from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_share_scope import DefaultShareScope
from openapi_server.models.share_permission import SharePermission
from openapi_server.models.share_permission_input_bean import SharePermissionInputBean
from openapi_server import util


async def add_share_permission(request: web.Request, id, body) -> web.Response:
    """Add share permission

    Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter.  Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put).  **[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

    :param id: The ID of the filter.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SharePermissionInputBean.from_dict(body)
    return web.Response(status=200)


async def delete_share_permission(request: web.Request, id, permission_id) -> web.Response:
    """Delete share permission

    Deletes a share permission from a filter.  **[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.

    :param id: The ID of the filter.
    :type id: int
    :param permission_id: The ID of the share permission.
    :type permission_id: int

    """
    return web.Response(status=200)


async def get_default_share_scope(request: web.Request, ) -> web.Response:
    """Get default share scope

    Returns the default sharing settings for new filters and dashboards for a user.  **[Permissions](#permissions) required:** Permission to access Jira.


    """
    return web.Response(status=200)


async def get_share_permission(request: web.Request, id, permission_id) -> web.Response:
    """Get share permission

    Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, a share permission is only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int
    :param permission_id: The ID of the share permission.
    :type permission_id: int

    """
    return web.Response(status=200)


async def get_share_permissions(request: web.Request, id) -> web.Response:
    """Get share permissions

    Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, share permissions are only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.

    :param id: The ID of the filter.
    :type id: int

    """
    return web.Response(status=200)


async def set_default_share_scope(request: web.Request, body) -> web.Response:
    """Set default share scope

    Sets the default sharing for new filters and dashboards for a user.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param body: 
    :type body: dict | bytes

    """
    body = DefaultShareScope.from_dict(body)
    return web.Response(status=200)
