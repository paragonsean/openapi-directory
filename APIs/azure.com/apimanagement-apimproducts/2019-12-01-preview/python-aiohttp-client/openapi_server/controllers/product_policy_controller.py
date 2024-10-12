from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_list_by_service_default_response import ProductListByServiceDefaultResponse
from openapi_server.models.product_policy_get200_response import ProductPolicyGet200Response
from openapi_server.models.product_policy_list_by_product200_response import ProductPolicyListByProduct200Response
from openapi_server import util


async def product_policy_create_or_update(request: web.Request, resource_group_name, service_name, product_id, policy_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """product_policy_create_or_update

    Creates or updates policy configuration for the Product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
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
    parameters = ProductPolicyGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def product_policy_delete(request: web.Request, resource_group_name, service_name, product_id, policy_id, if_match, api_version, subscription_id) -> web.Response:
    """product_policy_delete

    Deletes the policy configuration at the Product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
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


async def product_policy_get(request: web.Request, resource_group_name, service_name, product_id, policy_id, api_version, subscription_id, format=None) -> web.Response:
    """product_policy_get

    Get the policy configuration at the Product level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
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


async def product_policy_get_entity_tag(request: web.Request, resource_group_name, service_name, product_id, policy_id, api_version, subscription_id) -> web.Response:
    """product_policy_get_entity_tag

    Get the ETag of the policy configuration at the Product level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_policy_list_by_product(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id) -> web.Response:
    """product_policy_list_by_product

    Get the policy configuration at the Product level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
