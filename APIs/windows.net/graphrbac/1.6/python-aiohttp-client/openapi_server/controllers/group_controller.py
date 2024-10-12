from typing import List, Dict
from aiohttp import web

from openapi_server.models.ad_group import ADGroup
from openapi_server.models.check_group_membership_parameters import CheckGroupMembershipParameters
from openapi_server.models.check_group_membership_result import CheckGroupMembershipResult
from openapi_server.models.directory_object_list_result import DirectoryObjectListResult
from openapi_server.models.graph_error import GraphError
from openapi_server.models.group_add_member_parameters import GroupAddMemberParameters
from openapi_server.models.group_create_parameters import GroupCreateParameters
from openapi_server.models.group_get_member_groups_parameters import GroupGetMemberGroupsParameters
from openapi_server.models.group_get_member_groups_result import GroupGetMemberGroupsResult
from openapi_server.models.group_list_result import GroupListResult
from openapi_server import util


async def groups_add_member(request: web.Request, group_object_id, api_version, tenant_id, body) -> web.Response:
    """groups_add_member

    Add a member to a group.

    :param group_object_id: The object ID of the group to which to add the member.
    :type group_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The URL of the member object, such as https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd.
    :type body: dict | bytes

    """
    body = GroupAddMemberParameters.from_dict(body)
    return web.Response(status=200)


async def groups_create(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """groups_create

    Create a group in the directory.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The parameters for the group to create.
    :type body: dict | bytes

    """
    body = GroupCreateParameters.from_dict(body)
    return web.Response(status=200)


async def groups_delete(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """groups_delete

    Delete a group from the directory.

    :param object_id: The object ID of the group to delete.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def groups_get(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """groups_get

    Gets group information from the directory.

    :param object_id: The object ID of the user for which to get group information.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def groups_get_group_members(request: web.Request, object_id, api_version, tenant_id) -> web.Response:
    """groups_get_group_members

    Gets the members of a group.

    :param object_id: The object ID of the group whose members should be retrieved.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def groups_get_member_groups(request: web.Request, object_id, api_version, tenant_id, body) -> web.Response:
    """groups_get_member_groups

    Gets a collection of object IDs of groups of which the specified group is a member.

    :param object_id: The object ID of the group for which to get group membership.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Group filtering parameters.
    :type body: dict | bytes

    """
    body = GroupGetMemberGroupsParameters.from_dict(body)
    return web.Response(status=200)


async def groups_is_member_of(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """groups_is_member_of

    Checks whether the specified user, group, contact, or service principal is a direct or transitive member of the specified group.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: The check group membership parameters.
    :type body: dict | bytes

    """
    body = CheckGroupMembershipParameters.from_dict(body)
    return web.Response(status=200)


async def groups_list(request: web.Request, api_version, tenant_id, filter=None) -> web.Response:
    """groups_list

    Gets list of groups for the current tenant.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def groups_remove_member(request: web.Request, group_object_id, member_object_id, api_version, tenant_id) -> web.Response:
    """groups_remove_member

    Remove a member from a group.

    :param group_object_id: The object ID of the group from which to remove the member.
    :type group_object_id: str
    :param member_object_id: Member object id
    :type member_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)
