from typing import List, Dict
from aiohttp import web

from openapi_server.models.access_policy_response import AccessPolicyResponse
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.factory import Factory
from openapi_server.models.factory_list_response import FactoryListResponse
from openapi_server.models.factory_repo_update import FactoryRepoUpdate
from openapi_server.models.factory_update_parameters import FactoryUpdateParameters
from openapi_server.models.git_hub_access_token_request import GitHubAccessTokenRequest
from openapi_server.models.git_hub_access_token_response import GitHubAccessTokenResponse
from openapi_server.models.user_access_policy import UserAccessPolicy
from openapi_server import util


async def factories_configure_factory_repo(request: web.Request, subscription_id, location_id, api_version, factory_repo_update) -> web.Response:
    """factories_configure_factory_repo

    Updates a factory&#39;s repo information.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param location_id: The location identifier.
    :type location_id: str
    :param api_version: The API version.
    :type api_version: str
    :param factory_repo_update: Update factory repo request definition.
    :type factory_repo_update: dict | bytes

    """
    factory_repo_update = FactoryRepoUpdate.from_dict(factory_repo_update)
    return web.Response(status=200)


async def factories_create_or_update(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, factory, if_match=None) -> web.Response:
    """factories_create_or_update

    Creates or updates a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param factory: Factory resource definition.
    :type factory: dict | bytes
    :param if_match: ETag of the factory entity. Should only be specified for update, for which it should match existing entity or can be * for unconditional update.
    :type if_match: str

    """
    factory = Factory.from_dict(factory)
    return web.Response(status=200)


async def factories_delete(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """factories_delete

    Deletes a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def factories_get(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, if_none_match=None) -> web.Response:
    """factories_get

    Gets a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param if_none_match: ETag of the factory entity. Should only be specified for get. If the ETag matches the existing entity tag, or if * was provided, then no content will be returned.
    :type if_none_match: str

    """
    return web.Response(status=200)


async def factories_get_data_plane_access(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, policy) -> web.Response:
    """factories_get_data_plane_access

    Get Data Plane access.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param policy: Data Plane user access policy definition.
    :type policy: dict | bytes

    """
    policy = UserAccessPolicy.from_dict(policy)
    return web.Response(status=200)


async def factories_get_git_hub_access_token(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, git_hub_access_token_request) -> web.Response:
    """factories_get_git_hub_access_token

    Get GitHub Access Token.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param git_hub_access_token_request: Get GitHub access token request definition.
    :type git_hub_access_token_request: dict | bytes

    """
    git_hub_access_token_request = GitHubAccessTokenRequest.from_dict(git_hub_access_token_request)
    return web.Response(status=200)


async def factories_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """factories_list

    Lists factories under the specified subscription.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def factories_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """factories_list_by_resource_group

    Lists factories.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def factories_update(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, factory_update_parameters) -> web.Response:
    """factories_update

    Updates a factory.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param factory_update_parameters: The parameters for updating a factory.
    :type factory_update_parameters: dict | bytes

    """
    factory_update_parameters = FactoryUpdateParameters.from_dict(factory_update_parameters)
    return web.Response(status=200)
