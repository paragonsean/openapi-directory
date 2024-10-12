from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_resource import ProductResource
from openapi_server.models.product_resources_page import ProductResourcesPage
from openapi_server.models.products_download200_response import ProductsDownload200Response
from openapi_server import util


async def products_download(request: web.Request, subscription_id, resource_group, activation_name, product_name, api_version) -> web.Response:
    """products_download

    Downloads a product from azure marketplace.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: The resource group the resource is located under.
    :type resource_group: str
    :param activation_name: Name of the activation.
    :type activation_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_get(request: web.Request, subscription_id, resource_group, activation_name, product_name, api_version) -> web.Response:
    """products_get

    Return product name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: The resource group the resource is located under.
    :type resource_group: str
    :param activation_name: Name of the activation.
    :type activation_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_list(request: web.Request, subscription_id, resource_group, activation_name, api_version) -> web.Response:
    """products_list

    Return product name.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: The resource group the resource is located under.
    :type resource_group: str
    :param activation_name: Name of the activation.
    :type activation_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
