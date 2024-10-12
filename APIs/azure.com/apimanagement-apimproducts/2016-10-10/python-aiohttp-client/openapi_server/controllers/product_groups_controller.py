from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_groups_list_by_products200_response import ProductGroupsListByProducts200Response
from openapi_server.models.products_list_by_service_default_response import ProductsListByServiceDefaultResponse
from openapi_server import util


async def product_groups_create(request: web.Request, resource_group_name, service_name, product_id, group_id, api_version, subscription_id) -> web.Response:
    """product_groups_create

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


async def product_groups_delete(request: web.Request, resource_group_name, service_name, product_id, group_id, api_version, subscription_id) -> web.Response:
    """product_groups_delete

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


async def product_groups_list_by_products(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """product_groups_list_by_products

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
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | type        | eq, ne                 | N/A                                         |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
