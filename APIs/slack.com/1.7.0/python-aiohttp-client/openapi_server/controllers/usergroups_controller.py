from typing import List, Dict
from aiohttp import web

from openapi_server.models.usergroups_create_error_schema import UsergroupsCreateErrorSchema
from openapi_server.models.usergroups_create_schema import UsergroupsCreateSchema
from openapi_server.models.usergroups_disable_error_schema import UsergroupsDisableErrorSchema
from openapi_server.models.usergroups_disable_schema import UsergroupsDisableSchema
from openapi_server.models.usergroups_enable_error_schema import UsergroupsEnableErrorSchema
from openapi_server.models.usergroups_enable_schema import UsergroupsEnableSchema
from openapi_server.models.usergroups_list_error_schema import UsergroupsListErrorSchema
from openapi_server.models.usergroups_list_schema import UsergroupsListSchema
from openapi_server.models.usergroups_update_error_schema import UsergroupsUpdateErrorSchema
from openapi_server.models.usergroups_update_schema import UsergroupsUpdateSchema
from openapi_server.models.usergroups_users_list_error_schema import UsergroupsUsersListErrorSchema
from openapi_server.models.usergroups_users_list_schema import UsergroupsUsersListSchema
from openapi_server.models.usergroups_users_update_error_schema import UsergroupsUsersUpdateErrorSchema
from openapi_server.models.usergroups_users_update_schema import UsergroupsUsersUpdateSchema
from openapi_server import util


async def usergroups_create(request: web.Request, token, name, channels=None, description=None, handle=None, include_count=None) -> web.Response:
    """usergroups_create

    Create a User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:write&#x60;
    :type token: str
    :param name: A name for the User Group. Must be unique among User Groups.
    :type name: str
    :param channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
    :type channels: str
    :param description: A short description of the User Group.
    :type description: str
    :param handle: A mention handle. Must be unique among channels, users and User Groups.
    :type handle: str
    :param include_count: Include the number of users in each User Group.
    :type include_count: bool

    """
    return web.Response(status=200)


async def usergroups_disable(request: web.Request, token, usergroup, include_count=None) -> web.Response:
    """usergroups_disable

    Disable an existing User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:write&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to disable.
    :type usergroup: str
    :param include_count: Include the number of users in the User Group.
    :type include_count: bool

    """
    return web.Response(status=200)


async def usergroups_enable(request: web.Request, token, usergroup, include_count=None) -> web.Response:
    """usergroups_enable

    Enable a User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:write&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to enable.
    :type usergroup: str
    :param include_count: Include the number of users in the User Group.
    :type include_count: bool

    """
    return web.Response(status=200)


async def usergroups_list(request: web.Request, token, include_users=None, include_count=None, include_disabled=None) -> web.Response:
    """usergroups_list

    List all User Groups for a team

    :param token: Authentication token. Requires scope: &#x60;usergroups:read&#x60;
    :type token: str
    :param include_users: Include the list of users for each User Group.
    :type include_users: bool
    :param include_count: Include the number of users in each User Group.
    :type include_count: bool
    :param include_disabled: Include disabled User Groups.
    :type include_disabled: bool

    """
    return web.Response(status=200)


async def usergroups_update(request: web.Request, token, usergroup, channels=None, description=None, handle=None, include_count=None, name=None) -> web.Response:
    """usergroups_update

    Update an existing User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:write&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to update.
    :type usergroup: str
    :param channels: A comma separated string of encoded channel IDs for which the User Group uses as a default.
    :type channels: str
    :param description: A short description of the User Group.
    :type description: str
    :param handle: A mention handle. Must be unique among channels, users and User Groups.
    :type handle: str
    :param include_count: Include the number of users in the User Group.
    :type include_count: bool
    :param name: A name for the User Group. Must be unique among User Groups.
    :type name: str

    """
    return web.Response(status=200)


async def usergroups_users_list_0(request: web.Request, token, usergroup, include_disabled=None) -> web.Response:
    """usergroups_users_list_0

    List all users in a User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:read&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to update.
    :type usergroup: str
    :param include_disabled: Allow results that involve disabled User Groups.
    :type include_disabled: bool

    """
    return web.Response(status=200)


async def usergroups_users_update_0(request: web.Request, token, usergroup, users, include_count=None) -> web.Response:
    """usergroups_users_update_0

    Update the list of users for a User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:write&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to update.
    :type usergroup: str
    :param users: A comma separated string of encoded user IDs that represent the entire list of users for the User Group.
    :type users: str
    :param include_count: Include the number of users in the User Group.
    :type include_count: bool

    """
    return web.Response(status=200)
