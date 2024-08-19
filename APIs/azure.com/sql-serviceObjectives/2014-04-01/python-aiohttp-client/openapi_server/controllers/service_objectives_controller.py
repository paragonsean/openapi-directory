from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_objective import ServiceObjective
from openapi_server.models.service_objective_list_result import ServiceObjectiveListResult
from openapi_server import util


async def service_objectives_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, service_objective_name) -> web.Response:
    """service_objectives_get

    Gets a database service objective.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param service_objective_name: The name of the service objective to retrieve.
    :type service_objective_name: str

    """
    return web.Response(status=200)


async def service_objectives_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """service_objectives_list_by_server

    Returns database service objectives.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
