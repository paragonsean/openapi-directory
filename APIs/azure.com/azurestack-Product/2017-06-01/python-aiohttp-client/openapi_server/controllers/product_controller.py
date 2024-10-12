from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_configuration import DeviceConfiguration
from openapi_server.models.extended_product import ExtendedProduct
from openapi_server.models.marketplace_product_log_update import MarketplaceProductLogUpdate
from openapi_server.models.product import Product
from openapi_server.models.product_list import ProductList
from openapi_server.models.product_log import ProductLog
from openapi_server.models.products_list_default_response import ProductsListDefaultResponse
from openapi_server import util


async def products_get(request: web.Request, subscription_id, resource_group, registration_name, product_name, api_version) -> web.Response:
    """products_get

    Returns the specified product.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_get_product(request: web.Request, subscription_id, resource_group, registration_name, product_name, api_version, device_configuration=None) -> web.Response:
    """products_get_product

    Returns the specified product.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param device_configuration: Device configuration.
    :type device_configuration: dict | bytes

    """
    device_configuration = DeviceConfiguration.from_dict(device_configuration)
    return web.Response(status=200)


async def products_get_products(request: web.Request, subscription_id, resource_group, registration_name, api_version, device_configuration=None) -> web.Response:
    """products_get_products

    Returns a list of products.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param device_configuration: Device configuration.
    :type device_configuration: dict | bytes

    """
    device_configuration = DeviceConfiguration.from_dict(device_configuration)
    return web.Response(status=200)


async def products_list(request: web.Request, subscription_id, resource_group, registration_name, api_version) -> web.Response:
    """products_list

    Returns a list of products.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_list_details(request: web.Request, subscription_id, resource_group, registration_name, product_name, api_version) -> web.Response:
    """products_list_details

    Returns the extended properties of a product.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def products_upload_log(request: web.Request, subscription_id, resource_group, registration_name, product_name, api_version, marketplace_product_log_update=None) -> web.Response:
    """products_upload_log

    Returns the specified product.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param product_name: Name of the product.
    :type product_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param marketplace_product_log_update: Update details for product log.
    :type marketplace_product_log_update: dict | bytes

    """
    marketplace_product_log_update = MarketplaceProductLogUpdate.from_dict(marketplace_product_log_update)
    return web.Response(status=200)
