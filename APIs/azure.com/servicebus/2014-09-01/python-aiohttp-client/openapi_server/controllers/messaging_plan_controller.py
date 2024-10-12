from typing import List, Dict
from aiohttp import web

from openapi_server.models.messaging_plan import MessagingPlan
from openapi_server import util


async def messaging_plan_create_or_update(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id, parameters) -> web.Response:
    """messaging_plan_create_or_update

    Creates or updates a Messaging Plan for a namespace

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name.
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to create a messaging plan.
    :type parameters: dict | bytes

    """
    parameters = MessagingPlan.from_dict(parameters)
    return web.Response(status=200)


async def messaging_plan_get(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """messaging_plan_get

    Gets a description for the specified namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
