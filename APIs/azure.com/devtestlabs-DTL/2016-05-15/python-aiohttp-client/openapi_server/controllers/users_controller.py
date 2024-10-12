from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.response_with_continuation_user import ResponseWithContinuationUser
from openapi_server.models.user import User
from openapi_server.models.user_fragment import UserFragment
from openapi_server import util


async def users_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, user) -> web.Response:
    """users_create_or_update

    Create or replace an existing user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the user profile.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param user: Profile of a lab user.
    :type user: dict | bytes

    """
    user = User.from_dict(user)
    return web.Response(status=200)


async def users_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """users_delete

    Delete user profile. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the user profile.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def users_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """users_get

    Get user profile.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the user profile.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;identity)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def users_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """users_list

    List user profiles in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;identity)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def users_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, user) -> web.Response:
    """users_update

    Modify properties of user profiles.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the user profile.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param user: Profile of a lab user.
    :type user: dict | bytes

    """
    user = UserFragment.from_dict(user)
    return web.Response(status=200)
