from typing import List, Dict
from aiohttp import web

from openapi_server.models.current_user_identity import CurrentUserIdentity
from openapi_server.models.generate_sso_url_result import GenerateSsoUrlResult
from openapi_server.models.user_collection import UserCollection
from openapi_server.models.user_contract import UserContract
from openapi_server.models.user_create_parameters import UserCreateParameters
from openapi_server.models.user_get_identity_default_response import UserGetIdentityDefaultResponse
from openapi_server.models.user_token_parameters import UserTokenParameters
from openapi_server.models.user_token_result import UserTokenResult
from openapi_server.models.user_update_parameters import UserUpdateParameters
from openapi_server import util


async def user_create_or_update(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """user_create_or_update

    Creates or Updates a user.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = UserCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def user_delete(request: web.Request, resource_group_name, service_name, uid, if_match, api_version, subscription_id, delete_subscriptions=None, notify=None) -> web.Response:
    """user_delete

    Deletes specific user.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
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


async def user_generate_sso_url(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id) -> web.Response:
    """user_generate_sso_url

    Retrieves a redirection URL containing an authentication token for signing a given user into the developer portal.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_get(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id) -> web.Response:
    """user_get

    Gets the details of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_get_entity_tag(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id) -> web.Response:
    """user_get_entity_tag

    Gets the entity state (Etag) version of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_get_identity(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """user_get_identity

    Returns calling user identity information.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def user_get_shared_access_token(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id, parameters) -> web.Response:
    """user_get_shared_access_token

    Gets the Shared Access Authorization Token for the User.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create Authorization Token parameters.
    :type parameters: dict | bytes

    """
    parameters = UserTokenParameters.from_dict(parameters)
    return web.Response(status=200)


async def user_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
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
    :param filter: | Field            | Supported operators    | Supported functions               | |------------------|------------------------|-----------------------------------| | id               | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | firstName        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | lastName         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | email            | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state            | eq                     | N/A                               | | registrationDate | ge, le, eq, ne, gt, lt | N/A                               | | note             | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def user_update(request: web.Request, resource_group_name, service_name, uid, if_match, api_version, subscription_id, parameters) -> web.Response:
    """user_update

    Updates the details of the user specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = UserUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
