from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_get200_response import PolicyGet200Response
from openapi_server.models.policy_list_by_service200_response import PolicyListByService200Response
from openapi_server.models.policy_list_by_service_default_response import PolicyListByServiceDefaultResponse
from openapi_server import util


async def policy_create_or_update(request: web.Request, resource_group_name, service_name, policy_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """policy_create_or_update

    Creates or updates the global policy configuration of the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = PolicyGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def policy_delete(request: web.Request, resource_group_name, service_name, policy_id, if_match, api_version, subscription_id) -> web.Response:
    """policy_delete

    Deletes the global policy configuration of the Api Management Service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_get(request: web.Request, resource_group_name, service_name, policy_id, api_version, subscription_id, format=None) -> web.Response:
    """policy_get

    Get the Global policy definition of the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param format: Policy Export Format.
    :type format: str

    """
    return web.Response(status=200)


async def policy_get_entity_tag(request: web.Request, resource_group_name, service_name, policy_id, api_version, subscription_id) -> web.Response:
    """policy_get_entity_tag

    Gets the entity state (Etag) version of the Global policy definition in the Api Management service.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def policy_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """policy_list_by_service

    Lists all the Global Policy definitions of the Api Management service.

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
