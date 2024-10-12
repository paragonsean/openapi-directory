from typing import List, Dict
from aiohttp import web

from openapi_server.models.identity_provider_get200_response import IdentityProviderGet200Response
from openapi_server.models.identity_provider_list_by_service200_response import IdentityProviderListByService200Response
from openapi_server.models.identity_provider_list_by_service_default_response import IdentityProviderListByServiceDefaultResponse
from openapi_server.models.identity_provider_list_secrets200_response import IdentityProviderListSecrets200Response
from openapi_server.models.identity_provider_update_request import IdentityProviderUpdateRequest
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
    parameters = IdentityProviderGet200Response.from_dict(parameters)
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


async def identity_provider_get(request: web.Request, resource_group_name, service_name, identity_provider_name, api_version, subscription_id) -> web.Response:
    """identity_provider_get

    Gets the configuration details of the identity Provider configured in specified service instance.

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

    """
    return web.Response(status=200)


async def identity_provider_get_entity_tag(request: web.Request, resource_group_name, service_name, identity_provider_name, api_version, subscription_id) -> web.Response:
    """identity_provider_get_entity_tag

    Gets the entity state (Etag) version of the identityProvider specified by its identifier.

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

    """
    return web.Response(status=200)


async def identity_provider_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """identity_provider_list_by_service

    Lists a collection of Identity Provider configured in the specified service instance.

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


async def identity_provider_list_secrets(request: web.Request, resource_group_name, service_name, identity_provider_name, api_version, subscription_id) -> web.Response:
    """identity_provider_list_secrets

    Gets the client secret details of the Identity Provider.

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

    """
    return web.Response(status=200)


async def identity_provider_update(request: web.Request, resource_group_name, service_name, identity_provider_name, if_match, api_version, subscription_id, parameters) -> web.Response:
    """identity_provider_update

    Updates an existing IdentityProvider configuration.

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
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = IdentityProviderUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
