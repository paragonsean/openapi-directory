from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.integration_runtime_nodes_get200_response import IntegrationRuntimeNodesGet200Response
from openapi_server.models.integration_runtime_nodes_get_ip_address200_response import IntegrationRuntimeNodesGetIpAddress200Response
from openapi_server.models.update_integration_runtime_node_request import UpdateIntegrationRuntimeNodeRequest
from openapi_server import util


async def integration_runtime_nodes_delete(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, node_name, api_version) -> web.Response:
    """integration_runtime_nodes_delete

    Deletes a self-hosted integration runtime node.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param node_name: The integration runtime node name.
    :type node_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtime_nodes_get(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, node_name, api_version) -> web.Response:
    """integration_runtime_nodes_get

    Gets a self-hosted integration runtime node.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param node_name: The integration runtime node name.
    :type node_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtime_nodes_get_ip_address(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, node_name, api_version) -> web.Response:
    """integration_runtime_nodes_get_ip_address

    Get the IP address of self-hosted integration runtime node.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param node_name: The integration runtime node name.
    :type node_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def integration_runtime_nodes_update(request: web.Request, subscription_id, resource_group_name, factory_name, integration_runtime_name, node_name, api_version, update_integration_runtime_node_request) -> web.Response:
    """integration_runtime_nodes_update

    Updates a self-hosted integration runtime node.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param integration_runtime_name: The integration runtime name.
    :type integration_runtime_name: str
    :param node_name: The integration runtime node name.
    :type node_name: str
    :param api_version: The API version.
    :type api_version: str
    :param update_integration_runtime_node_request: The parameters for updating an integration runtime node.
    :type update_integration_runtime_node_request: dict | bytes

    """
    update_integration_runtime_node_request = UpdateIntegrationRuntimeNodeRequest.from_dict(update_integration_runtime_node_request)
    return web.Response(status=200)
