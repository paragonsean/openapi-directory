from typing import List, Dict
from aiohttp import web

from openapi_server.models.products_list_by_service_default_response import ProductsListByServiceDefaultResponse
from openapi_server import util


async def product_policy_create_or_update(request: web.Request, resource_group_name, service_name, product_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """product_policy_create_or_update

    Creates or updates policy configuration for the Product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The policy contents to apply.
    :type parameters: 

    """
    return web.Response(status=200)


async def product_policy_delete(request: web.Request, resource_group_name, service_name, product_id, if_match, api_version, subscription_id) -> web.Response:
    """product_policy_delete

    Deletes the policy configuration at the Product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_policy_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id, product_id) -> web.Response:
    """product_policy_get

    Get the policy configuration at the Product level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str

    """
    return web.Response(status=200)
