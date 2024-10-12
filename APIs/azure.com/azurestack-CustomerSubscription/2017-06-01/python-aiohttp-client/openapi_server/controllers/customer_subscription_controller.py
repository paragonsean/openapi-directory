from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_subscription import CustomerSubscription
from openapi_server.models.customer_subscription_list import CustomerSubscriptionList
from openapi_server.models.customer_subscriptions_list_default_response import CustomerSubscriptionsListDefaultResponse
from openapi_server import util


async def customer_subscriptions_create(request: web.Request, subscription_id, resource_group, registration_name, customer_subscription_name, api_version, customer_creation_parameters) -> web.Response:
    """customer_subscriptions_create

    Creates a new customer subscription under a registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param customer_subscription_name: Name of the product.
    :type customer_subscription_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param customer_creation_parameters: Parameters use to create a customer subscription.
    :type customer_creation_parameters: dict | bytes

    """
    customer_creation_parameters = CustomerSubscription.from_dict(customer_creation_parameters)
    return web.Response(status=200)


async def customer_subscriptions_delete(request: web.Request, subscription_id, resource_group, registration_name, customer_subscription_name, api_version) -> web.Response:
    """customer_subscriptions_delete

    Deletes a customer subscription under a registration.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param customer_subscription_name: Name of the product.
    :type customer_subscription_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def customer_subscriptions_get(request: web.Request, subscription_id, resource_group, registration_name, customer_subscription_name, api_version) -> web.Response:
    """customer_subscriptions_get

    Returns the specified product.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: Name of the resource group.
    :type resource_group: str
    :param registration_name: Name of the Azure Stack registration.
    :type registration_name: str
    :param customer_subscription_name: Name of the product.
    :type customer_subscription_name: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def customer_subscriptions_list(request: web.Request, subscription_id, resource_group, registration_name, api_version) -> web.Response:
    """customer_subscriptions_list

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
