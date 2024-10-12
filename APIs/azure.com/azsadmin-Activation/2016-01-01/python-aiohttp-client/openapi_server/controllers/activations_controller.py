from typing import List, Dict
from aiohttp import web

from openapi_server.models.activation import Activation
from openapi_server.models.activation_resource import ActivationResource
from openapi_server.models.activation_resources_page import ActivationResourcesPage
from openapi_server import util


async def activations_create_or_update(request: web.Request, subscription_id, resource_group, activation_name, api_version, activation) -> web.Response:
    """activations_create_or_update

    Create a new activation.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: The resource group the resource is located under.
    :type resource_group: str
    :param activation_name: Name of the activation.
    :type activation_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param activation: new activation.
    :type activation: dict | bytes

    """
    activation = Activation.from_dict(activation)
    return web.Response(status=200)


async def activations_delete(request: web.Request, subscription_id, resource_group, activation_name, api_version) -> web.Response:
    """activations_delete

    Delete an activation.

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


async def activations_get(request: web.Request, subscription_id, resource_group, activation_name, api_version) -> web.Response:
    """activations_get

    Returns activation name.

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


async def activations_list(request: web.Request, subscription_id, resource_group, api_version) -> web.Response:
    """activations_list

    Returns the list of activations.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group: The resource group the resource is located under.
    :type resource_group: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
