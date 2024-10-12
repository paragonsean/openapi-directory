from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_provider_contract import IdentityProviderContract
from openapi_server.models.identity_provider_list import IdentityProviderList
from openapi_server.models.identity_provider_list_by_service_default_response import IdentityProviderListByServiceDefaultResponse
from openapi_server import util


async def identity_provider_create_or_update(request: web.Request, resource_group_name, service_name, identity_provider_name, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """identity_provider_create_or_update

    Creates or Updates the IdentityProvider configuration.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param identity_provider_name: Identity Provider Type identifier.
    :type identity_provider_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = IdentityProviderContract.from_dict(parameters)
    return web.Response(status=200)


async def identity_provider_delete(request: web.Request, resource_group_name, service_name, identity_provider_name, if_match, api_version, subscription_id) -> web.Response:
    """identity_provider_delete

    Deletes the specified identity provider configuration.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param identity_provider_name: Identity Provider Type identifier.
    :type identity_provider_name: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def identity_provider_get(request: web.Request, subscription_id, resource_group_name, service_name, identity_provider_name, api_version) -> web.Response:
    """identity_provider_get

    Gets the configuration details of the identity Provider configured in specified service instance.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param identity_provider_name: Identity Provider Type identifier.
    :type identity_provider_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def identity_provider_get_entity_tag(request: web.Request, subscription_id, resource_group_name, service_name, identity_provider_name, api_version) -> web.Response:
    """identity_provider_get_entity_tag

    Gets the entity state (Etag) version of the identityProvider specified by its identifier.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param identity_provider_name: Identity Provider Type identifier.
    :type identity_provider_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def identity_provider_list_by_service(request: web.Request, subscription_id, resource_group_name, service_name, api_version) -> web.Response:
    """identity_provider_list_by_service

    Lists a collection of Identity Provider configured in the specified service instance.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
