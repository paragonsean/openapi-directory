from typing import List, Dict
from aiohttp import web

from openapi_server.models.corporate_account import CorporateAccount
from openapi_server.models.permission_list import PermissionList
from openapi_server.models.user import User
from openapi_server.models.user_group import UserGroup
from openapi_server.models.user_group_list import UserGroupList
from openapi_server.models.user_list import UserList
from openapi_server.models.user_update_content import UserUpdateContent
from openapi_server import util


async def get_available_corporate_permissions(request: web.Request, ) -> web.Response:
    """View available permissions

    View a list of available permissions for your corporate account. They are used when assigning permissions to your corporate users.


    """
    return web.Response(status=200)


async def get_available_corporate_permissions_by_id(request: web.Request, corporate_id) -> web.Response:
    """Get a list of available permissions for this corporate account. They are used when assigning permissions to corporate users.

    Get a list of available permissions for this corporate account. They are used when assigning permissions to corporate users.

    :param corporate_id: Corporate ID
    :type corporate_id: int

    """
    return web.Response(status=200)


async def get_corporate(request: web.Request, ) -> web.Response:
    """View your corporate account

    View the details of the corporate account that your user account belongs to.


    """
    return web.Response(status=200)


async def get_corporate_by_id(request: web.Request, corporate_id) -> web.Response:
    """Get details of this corporate account

    Get details of this corporate account

    :param corporate_id: Corporate ID
    :type corporate_id: int

    """
    return web.Response(status=200)


async def get_corporate_user_groups(request: web.Request, ) -> web.Response:
    """View user groups

    View a list of user groups under my corporate account. User groups are a part of our RBAC implementation and can be used to configure complex permission scenarios.


    """
    return web.Response(status=200)


async def get_corporate_user_groups_by_id(request: web.Request, corporate_id) -> web.Response:
    """Get a list of user groups for this corporate account

    Get a list of user groups for this corporate account

    :param corporate_id: Corporate ID
    :type corporate_id: int

    """
    return web.Response(status=200)


async def get_corporate_users(request: web.Request, ) -> web.Response:
    """View users

    View a list of users under your corporate account. This endpoint will only return information if your user account is permitted to view corporate account users, configured by your administrator.


    """
    return web.Response(status=200)


async def get_corporate_users_by_id(request: web.Request, corporate_id) -> web.Response:
    """Get a list of users for this corporate account

    Get a list of users for this corporate account

    :param corporate_id: Corporate ID
    :type corporate_id: int

    """
    return web.Response(status=200)


async def get_corporates_list(request: web.Request, ) -> web.Response:
    """Get a list of corporate accounts

    Get a list of corporate accounts


    """
    return web.Response(status=200)


async def save_corporate_user(request: web.Request, body) -> web.Response:
    """Create or update a user

    Create or update a user under your corporate account. This endpoint requires permissions for corporate user management, configured by your administrator.

    :param body: 
    :type body: dict | bytes

    """
    body = UserUpdateContent.from_dict(body)
    return web.Response(status=200)


async def save_corporate_user_group(request: web.Request, body) -> web.Response:
    """Create or update a corporate user group

    Create or update a corporate user group

    :param body: 
    :type body: dict | bytes

    """
    body = UserGroup.from_dict(body)
    return web.Response(status=200)


async def save_corporate_user_group_by_id(request: web.Request, corporate_id, body) -> web.Response:
    """Create or update a corporate user group for this corporate account

    Create or update a corporate user group for this corporate account

    :param corporate_id: Corporate ID
    :type corporate_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserGroup.from_dict(body)
    return web.Response(status=200)
