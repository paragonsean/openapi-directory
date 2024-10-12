from typing import List, Dict
from aiohttp import web

from openapi_server.models.usergroups_users_list_error_schema import UsergroupsUsersListErrorSchema
from openapi_server.models.usergroups_users_list_schema import UsergroupsUsersListSchema
from openapi_server.models.usergroups_users_update_error_schema import UsergroupsUsersUpdateErrorSchema
from openapi_server.models.usergroups_users_update_schema import UsergroupsUsersUpdateSchema
from openapi_server import util


async def usergroups_users_list(request: web.Request, token, usergroup, include_disabled=None) -> web.Response:
    """usergroups_users_list

    List all users in a User Group

    :param token: Authentication token. Requires scope: &#x60;usergroups:read&#x60;
    :type token: str
    :param usergroup: The encoded ID of the User Group to update.
    :type usergroup: str
    :param include_disabled: Allow results that involve disabled User Groups.
    :type include_disabled: bool

    """
    return web.Response(status=200)


async def usergroups_users_update(request: web.Request, token, usergroup, users, include_count=None) -> web.Response:
    """usergroups_users_update

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
