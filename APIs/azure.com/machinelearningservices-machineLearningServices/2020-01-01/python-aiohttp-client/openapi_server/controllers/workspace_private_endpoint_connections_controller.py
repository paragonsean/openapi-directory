from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.private_endpoint_connection import PrivateEndpointConnection
from openapi_server import util


async def private_endpoint_connections_delete(request: web.Request, subscription_id, resource_group_name, workspace_name, private_endpoint_connection_name, api_version) -> web.Response:
    """private_endpoint_connections_delete

    Deletes the specified private endpoint connection associated with the workspace.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the workspace
    :type private_endpoint_connection_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_get(request: web.Request, subscription_id, resource_group_name, workspace_name, private_endpoint_connection_name, api_version) -> web.Response:
    """private_endpoint_connections_get

    Gets the specified private endpoint connection associated with the workspace.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the workspace
    :type private_endpoint_connection_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str

    """
    return web.Response(status=200)


async def private_endpoint_connections_put(request: web.Request, subscription_id, resource_group_name, workspace_name, private_endpoint_connection_name, api_version, properties) -> web.Response:
    """private_endpoint_connections_put

    Update the state of specified private endpoint connection associated with the workspace.

    :param subscription_id: Azure subscription identifier.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group in which workspace is located.
    :type resource_group_name: str
    :param workspace_name: Name of Azure Machine Learning workspace.
    :type workspace_name: str
    :param private_endpoint_connection_name: The name of the private endpoint connection associated with the workspace
    :type private_endpoint_connection_name: str
    :param api_version: Version of Azure Machine Learning resource provider API.
    :type api_version: str
    :param properties: The private endpoint connection properties.
    :type properties: dict | bytes

    """
    properties = PrivateEndpointConnection.from_dict(properties)
    return web.Response(status=200)
