from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_group_create_or_update200_response import ProductGroupCreateOrUpdate200Response
from openapi_server.models.product_group_list_by_product200_response import ProductGroupListByProduct200Response
from openapi_server.models.product_list_by_service_default_response import ProductListByServiceDefaultResponse
from openapi_server import util


async def product_group_check_entity_exists(request: web.Request, resource_group_name, service_name, product_id, group_id, api_version, subscription_id) -> web.Response:
    """product_group_check_entity_exists

    Checks that Group entity specified by identifier is associated with the Product entity.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_group_create_or_update(request: web.Request, resource_group_name, service_name, product_id, group_id, api_version, subscription_id) -> web.Response:
    """product_group_create_or_update

    Adds the association between the specified developer group with the specified product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_group_delete(request: web.Request, resource_group_name, service_name, product_id, group_id, api_version, subscription_id) -> web.Response:
    """product_group_delete

    Deletes the association between the specified group and product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_group_list_by_product(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """product_group_list_by_product

    Lists the collection of developer groups associated with the specified product.

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
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt |     | &lt;/br&gt;| displayName | filter | eq, ne |     | &lt;/br&gt;| description | filter | eq, ne |     | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
