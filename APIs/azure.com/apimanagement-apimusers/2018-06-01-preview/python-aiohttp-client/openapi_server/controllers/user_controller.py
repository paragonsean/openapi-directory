from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_create_or_update_request import UserCreateOrUpdateRequest
from openapi_server.models.user_get200_response import UserGet200Response
from openapi_server.models.user_list_by_service200_response import UserListByService200Response
from openapi_server.models.user_list_by_service_default_response import UserListByServiceDefaultResponse
from openapi_server.models.user_update_request import UserUpdateRequest
from openapi_server import util


async def user_create_or_update(request: web.Request, resource_group_name, service_name, user_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """user_create_or_update

    Creates or Updates a user.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = UserCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)


async def user_delete(request: web.Request, resource_group_name, service_name, user_id, if_match, api_version, subscription_id, delete_subscriptions=None, notify=None) -> web.Response:
    """user_delete

    Deletes specific user.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delete_subscriptions: Whether to delete user&#39;s subscription or not.
    :type delete_subscriptions: bool
    :param notify: Send an Account Closed Email notification to the User.
    :type notify: bool

    """
    return web.Response(status=200)


async def user_get(request: web.Request, resource_group_name, service_name, user_id, api_version, subscription_id) -> web.Response:
    """user_get

    Gets the details of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_get_entity_tag(request: web.Request, resource_group_name, service_name, user_id, api_version, subscription_id) -> web.Response:
    """user_get_entity_tag

    Gets the entity state (Etag) version of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, expand_groups=None) -> web.Response:
    """user_list_by_service

    Lists a collection of registered users in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |firstName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |lastName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |email | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |registrationDate | ge, le, eq, ne, gt, lt |    | |note | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |groups |     |    | 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param expand_groups: 
    :type expand_groups: bool

    """
    return web.Response(status=200)


async def user_update(request: web.Request, resource_group_name, service_name, user_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """user_update

    Updates the details of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = UserUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
