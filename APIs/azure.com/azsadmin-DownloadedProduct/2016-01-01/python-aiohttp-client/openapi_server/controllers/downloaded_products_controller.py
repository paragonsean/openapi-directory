from typing import List, Dict
from aiohttp import web

from openapi_server.models.downloaded_product_resources_page import DownloadedProductResourcesPage
from openapi_server.models.downloaded_products_get200_response import DownloadedProductsGet200Response
from openapi_server import util


async def downloaded_products_create(request: web.Request, subscription_id, resource_group, activation_name, product_name, api_version, downloaded_product) -> web.Response:
    """downloaded_products_create

    Creates a downloaded product.

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
    :param downloaded_product: Downloaded product resource definition.
    :type downloaded_product: dict | bytes

    """
    downloaded_product = DownloadedProductsGet200Response.from_dict(downloaded_product)
    return web.Response(status=200)


async def downloaded_products_delete(request: web.Request, subscription_id, resource_group, activation_name, product_name, api_version) -> web.Response:
    """downloaded_products_delete

    Delete a downloaded product.

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


async def downloaded_products_get(request: web.Request, subscription_id, resource_group, activation_name, product_name, api_version) -> web.Response:
    """downloaded_products_get

    Get a downloaded product.

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


async def downloaded_products_list(request: web.Request, subscription_id, resource_group, activation_name, api_version) -> web.Response:
    """downloaded_products_list

    Get a list of downloaded products.

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
