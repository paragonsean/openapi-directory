from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_pool import AgentPool
from openapi_server.models.agent_pool_list_result import AgentPoolListResult
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def agent_pools_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, agent_pool_name, parameters) -> web.Response:
    """Creates or updates an agent pool.

    Creates or updates an agent pool in the specified managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param agent_pool_name: The name of the agent pool.
    :type agent_pool_name: str
    :param parameters: Parameters supplied to the Create or Update an agent pool operation.
    :type parameters: dict | bytes

    """
    parameters = AgentPool.from_dict(parameters)
    return web.Response(status=200)


async def agent_pools_delete(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, agent_pool_name) -> web.Response:
    """Deletes an agent pool.

    Deletes the agent pool in the specified managed cluster.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param agent_pool_name: The name of the agent pool.
    :type agent_pool_name: str

    """
    return web.Response(status=200)


async def agent_pools_get(request: web.Request, api_version, subscription_id, resource_group_name, resource_name, agent_pool_name) -> web.Response:
    """Gets the agent pool.

    Gets the details of the agent pool by managed cluster and resource group.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str
    :param agent_pool_name: The name of the agent pool.
    :type agent_pool_name: str

    """
    return web.Response(status=200)


async def agent_pools_list(request: web.Request, api_version, subscription_id, resource_group_name, resource_name) -> web.Response:
    """Gets a list of agent pools in the specified managed cluster.

    Gets a list of agent pools in the specified managed cluster. The operation returns properties of each agent pool.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param resource_name: The name of the managed cluster resource.
    :type resource_name: str

    """
    return web.Response(status=200)
