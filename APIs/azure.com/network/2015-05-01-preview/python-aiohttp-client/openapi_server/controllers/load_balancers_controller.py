from typing import List, Dict
from aiohttp import web

from openapi_server.models.load_balancer import LoadBalancer
from openapi_server.models.load_balancer_list_result import LoadBalancerListResult
from openapi_server import util


async def load_balancers_create_or_update(request: web.Request, resource_group_name, load_balancer_name, api_version, subscription_id, parameters) -> web.Response:
    """load_balancers_create_or_update

    The Put LoadBalancer operation creates/updates a LoadBalancer

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param load_balancer_name: The name of the loadBalancer.
    :type load_balancer_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/delete LoadBalancer operation
    :type parameters: dict | bytes

    """
    parameters = LoadBalancer.from_dict(parameters)
    return web.Response(status=200)


async def load_balancers_delete(request: web.Request, resource_group_name, load_balancer_name, api_version, subscription_id) -> web.Response:
    """load_balancers_delete

    The delete loadbalancer operation deletes the specified loadbalancer.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param load_balancer_name: The name of the loadBalancer.
    :type load_balancer_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def load_balancers_get(request: web.Request, resource_group_name, load_balancer_name, api_version, subscription_id) -> web.Response:
    """load_balancers_get

    The Get network interface operation retrieves information about the specified network interface.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param load_balancer_name: The name of the loadBalancer.
    :type load_balancer_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def load_balancers_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """load_balancers_list

    The List loadBalancer operation retrieves all the load balancers in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def load_balancers_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """load_balancers_list_all

    The List loadBalancer operation retrieves all the load balancers in a subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
