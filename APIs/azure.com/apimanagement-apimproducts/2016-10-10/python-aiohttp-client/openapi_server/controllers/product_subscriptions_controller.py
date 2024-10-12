from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_subscriptions_list_by_products200_response import ProductSubscriptionsListByProducts200Response
from openapi_server.models.products_list_by_service_default_response import ProductsListByServiceDefaultResponse
from openapi_server import util


async def product_subscriptions_list_by_products(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """product_subscriptions_list_by_products

    Lists the collection of subscriptions to the specified product.

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
    :param filter: | Field        | Supported operators    | Supported functions                         | |--------------|------------------------|---------------------------------------------| | id           | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name         | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | stateComment | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | userId       | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | productId    | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | state        | eq                     |                                             |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
