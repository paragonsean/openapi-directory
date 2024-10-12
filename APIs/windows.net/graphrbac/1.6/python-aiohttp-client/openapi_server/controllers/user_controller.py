from typing import List, Dict
from aiohttp import web

from openapi_server.models.graph_error import GraphError
from openapi_server.models.user import User
from openapi_server.models.user_create_parameters import UserCreateParameters
from openapi_server.models.user_get_member_groups_parameters import UserGetMemberGroupsParameters
from openapi_server.models.user_get_member_groups_result import UserGetMemberGroupsResult
from openapi_server.models.user_list_result import UserListResult
from openapi_server.models.user_update_parameters import UserUpdateParameters
from openapi_server import util


async def users_create(request: web.Request, api_version, tenant_id, body) -> web.Response:
    """users_create

    Create a new user.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to create a user.
    :type body: dict | bytes

    """
    body = UserCreateParameters.from_dict(body)
    return web.Response(status=200)


async def users_delete(request: web.Request, upn_or_object_id, api_version, tenant_id) -> web.Response:
    """users_delete

    Delete a user.

    :param upn_or_object_id: The object ID or principal name of the user to delete.
    :type upn_or_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def users_get(request: web.Request, upn_or_object_id, api_version, tenant_id) -> web.Response:
    """users_get

    Gets user information from the directory.

    :param upn_or_object_id: The object ID or principal name of the user for which to get information.
    :type upn_or_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str

    """
    return web.Response(status=200)


async def users_get_member_groups(request: web.Request, object_id, api_version, tenant_id, body) -> web.Response:
    """users_get_member_groups

    Gets a collection that contains the object IDs of the groups of which the user is a member.

    :param object_id: The object ID of the user for which to get group membership.
    :type object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: User filtering parameters.
    :type body: dict | bytes

    """
    body = UserGetMemberGroupsParameters.from_dict(body)
    return web.Response(status=200)


async def users_list(request: web.Request, api_version, tenant_id, filter=None, expand=None, top=None) -> web.Response:
    """users_list

    Gets list of users for the current tenant.

    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param expand: The expand value for the operation result.
    :type expand: str
    :param top: (Optional) Set the maximum number of results per response.
    :type top: int

    """
    return web.Response(status=200)


async def users_update(request: web.Request, upn_or_object_id, api_version, tenant_id, body) -> web.Response:
    """users_update

    Updates a user.

    :param upn_or_object_id: The object ID or principal name of the user to update.
    :type upn_or_object_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param tenant_id: The tenant ID.
    :type tenant_id: str
    :param body: Parameters to update an existing user.
    :type body: dict | bytes

    """
    body = UserUpdateParameters.from_dict(body)
    return web.Response(status=200)
