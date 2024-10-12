from typing import List, Dict
from aiohttp import web

from openapi_server.models.permission_grant import PermissionGrant
from openapi_server.models.permission_grants import PermissionGrants
from openapi_server.models.permission_scheme import PermissionScheme
from openapi_server.models.permission_schemes import PermissionSchemes
from openapi_server import util


async def create_permission_grant(request: web.Request, scheme_id, body, expand=None) -> web.Response:
    """Create permission grant

    Creates a permission grant in a permission scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param scheme_id: The ID of the permission scheme in which to create a new permission grant.
    :type scheme_id: int
    :param body: The permission grant to create.
    :type body: dict | bytes
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;all&#x60; Returns all expandable information.
    :type expand: str

    """
    body = PermissionGrant.from_dict(body)
    return web.Response(status=200)


async def create_permission_scheme(request: web.Request, body, expand=None) -> web.Response:
    """Create permission scheme

    Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param body: The permission scheme to create.
    :type body: dict | bytes
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    body = PermissionScheme.from_dict(body)
    return web.Response(status=200)


async def delete_permission_scheme(request: web.Request, scheme_id) -> web.Response:
    """Delete permission scheme

    Deletes a permission scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param scheme_id: The ID of the permission scheme being deleted.
    :type scheme_id: int

    """
    return web.Response(status=200)


async def delete_permission_scheme_entity(request: web.Request, scheme_id, permission_id) -> web.Response:
    """Delete permission scheme grant

    Deletes a permission grant from a permission scheme. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param scheme_id: The ID of the permission scheme to delete the permission grant from.
    :type scheme_id: int
    :param permission_id: The ID of the permission grant to delete.
    :type permission_id: int

    """
    return web.Response(status=200)


async def get_all_permission_schemes(request: web.Request, expand=None) -> web.Response:
    """Get all permission schemes

    Returns all permission schemes.  ### About permission schemes and grants ###  A permission scheme is a collection of permission grants. A permission grant consists of a &#x60;holder&#x60; and a &#x60;permission&#x60;.  #### Holder object ####  The &#x60;holder&#x60; object contains information about the user or group being granted the permission. For example, the *Administer projects* permission is granted to a group named *Teams in space administrators*. In this case, the type is &#x60;\&quot;type\&quot;: \&quot;group\&quot;&#x60;, and the parameter is the group name, &#x60;\&quot;parameter\&quot;: \&quot;Teams in space administrators\&quot;&#x60; and the value is group ID, &#x60;\&quot;value\&quot;: \&quot;ca85fac0-d974-40ca-a615-7af99c48d24f\&quot;&#x60;. The &#x60;holder&#x60; object is defined by the following properties:   *  &#x60;type&#x60; Identifies the user or group (see the list of types below).  *  &#x60;parameter&#x60; As a group&#39;s name can change, use of &#x60;value&#x60; is recommended. The value of this property depends on the &#x60;type&#x60;. For example, if the &#x60;type&#x60; is a group, then you need to specify the group name.  *  &#x60;value&#x60; The value of this property depends on the &#x60;type&#x60;. If the &#x60;type&#x60; is a group, then you need to specify the group ID. For other &#x60;type&#x60; it has the same value as &#x60;parameter&#x60;  The following &#x60;types&#x60; are available. The expected values for &#x60;parameter&#x60; and &#x60;value&#x60; are given in parentheses (some types may not have a &#x60;parameter&#x60; or &#x60;value&#x60;):   *  &#x60;anyone&#x60; Grant for anonymous users.  *  &#x60;applicationRole&#x60; Grant for users with access to the specified application (application name, application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL) for more information.  *  &#x60;assignee&#x60; Grant for the user currently assigned to an issue.  *  &#x60;group&#x60; Grant for the specified group (&#x60;parameter&#x60; : group name, &#x60;value&#x60; : group ID).  *  &#x60;groupCustomField&#x60; Grant for a user in the group selected in the specified custom field (&#x60;parameter&#x60; : custom field ID, &#x60;value&#x60; : custom field ID).  *  &#x60;projectLead&#x60; Grant for a project lead.  *  &#x60;projectRole&#x60; Grant for the specified project role (&#x60;parameter&#x60; :project role ID, &#x60;value&#x60; : project role ID).  *  &#x60;reporter&#x60; Grant for the user who reported the issue.  *  &#x60;sd.customer.portal.only&#x60; Jira Service Desk only. Grants customers permission to access the customer portal but not Jira. See [Customizing Jira Service Desk permissions](https://confluence.atlassian.com/x/24dKLg) for more information.  *  &#x60;user&#x60; Grant for the specified user (&#x60;parameter&#x60; : user ID - historically this was the userkey but that is deprecated and the account ID should be used, &#x60;value&#x60; : user ID).  *  &#x60;userCustomField&#x60; Grant for a user selected in the specified custom field (&#x60;parameter&#x60; : custom field ID, &#x60;value&#x60; : custom field ID).  #### Built-in permissions ####  The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps can also define custom permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information.  **Project permissions**   *  &#x60;ADMINISTER_PROJECTS&#x60;  *  &#x60;BROWSE_PROJECTS&#x60;  *  &#x60;MANAGE_SPRINTS_PERMISSION&#x60; (Jira Software only)  *  &#x60;SERVICEDESK_AGENT&#x60; (Jira Service Desk only)  *  &#x60;VIEW_DEV_TOOLS&#x60; (Jira Software only)  *  &#x60;VIEW_READONLY_WORKFLOW&#x60;  **Issue permissions**   *  &#x60;ASSIGNABLE_USER&#x60;  *  &#x60;ASSIGN_ISSUES&#x60;  *  &#x60;CLOSE_ISSUES&#x60;  *  &#x60;CREATE_ISSUES&#x60;  *  &#x60;DELETE_ISSUES&#x60;  *  &#x60;EDIT_ISSUES&#x60;  *  &#x60;LINK_ISSUES&#x60;  *  &#x60;MODIFY_REPORTER&#x60;  *  &#x60;MOVE_ISSUES&#x60;  *  &#x60;RESOLVE_ISSUES&#x60;  *  &#x60;SCHEDULE_ISSUES&#x60;  *  &#x60;SET_ISSUE_SECURITY&#x60;  *  &#x60;TRANSITION_ISSUES&#x60;  **Voters and watchers permissions**   *  &#x60;MANAGE_WATCHERS&#x60;  *  &#x60;VIEW_VOTERS_AND_WATCHERS&#x60;  **Comments permissions**   *  &#x60;ADD_COMMENTS&#x60;  *  &#x60;DELETE_ALL_COMMENTS&#x60;  *  &#x60;DELETE_OWN_COMMENTS&#x60;  *  &#x60;EDIT_ALL_COMMENTS&#x60;  *  &#x60;EDIT_OWN_COMMENTS&#x60;  **Attachments permissions**   *  &#x60;CREATE_ATTACHMENTS&#x60;  *  &#x60;DELETE_ALL_ATTACHMENTS&#x60;  *  &#x60;DELETE_OWN_ATTACHMENTS&#x60;  **Time tracking permissions**   *  &#x60;DELETE_ALL_WORKLOGS&#x60;  *  &#x60;DELETE_OWN_WORKLOGS&#x60;  *  &#x60;EDIT_ALL_WORKLOGS&#x60;  *  &#x60;EDIT_OWN_WORKLOGS&#x60;  *  &#x60;WORK_ON_ISSUES&#x60;  **[Permissions](#permissions) required:** Permission to access Jira.

    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_scheme(request: web.Request, scheme_id, expand=None) -> web.Response:
    """Get permission scheme

    Returns a permission scheme.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param scheme_id: The ID of the permission scheme to return.
    :type scheme_id: int
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_scheme_grant(request: web.Request, scheme_id, permission_id, expand=None) -> web.Response:
    """Get permission scheme grant

    Returns a permission grant.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param scheme_id: The ID of the permission scheme.
    :type scheme_id: int
    :param permission_id: The ID of the permission grant.
    :type permission_id: int
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    return web.Response(status=200)


async def get_permission_scheme_grants(request: web.Request, scheme_id, expand=None) -> web.Response:
    """Get permission scheme grants

    Returns all permission grants for a permission scheme.  **[Permissions](#permissions) required:** Permission to access Jira.

    :param scheme_id: The ID of the permission scheme.
    :type scheme_id: int
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;all&#x60; Returns all expandable information.
    :type expand: str

    """
    return web.Response(status=200)


async def update_permission_scheme(request: web.Request, scheme_id, body, expand=None) -> web.Response:
    """Update permission scheme

    Updates a permission scheme. Below are some important things to note when using this resource:   *  If a permissions list is present in the request, then it is set in the permission scheme, overwriting *all existing* grants.  *  If you want to update only the name and description, then do not send a permissions list in the request.  *  Sending an empty list will remove all permission grants from the permission scheme.  If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete).  See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    :param scheme_id: The ID of the permission scheme to update.
    :type scheme_id: int
    :param body: 
    :type body: dict | bytes
    :param expand: Use expand to include additional information in the response. This parameter accepts a comma-separated list. Note that permissions are always included when you specify any value. Expand options include:   *  &#x60;all&#x60; Returns all expandable information.  *  &#x60;field&#x60; Returns information about the custom field granted the permission.  *  &#x60;group&#x60; Returns information about the group that is granted the permission.  *  &#x60;permissions&#x60; Returns all permission grants for each permission scheme.  *  &#x60;projectRole&#x60; Returns information about the project role granted the permission.  *  &#x60;user&#x60; Returns information about the user who is granted the permission.
    :type expand: str

    """
    body = PermissionScheme.from_dict(body)
    return web.Response(status=200)
