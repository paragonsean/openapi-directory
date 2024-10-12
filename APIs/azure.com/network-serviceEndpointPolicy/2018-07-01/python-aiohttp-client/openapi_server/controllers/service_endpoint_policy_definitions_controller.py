from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_endpoint_policy_definition_list_result import ServiceEndpointPolicyDefinitionListResult
from openapi_server import util


async def service_endpoint_policy_definitions_delete(request: web.Request, resource_group_name, service_endpoint_policy_name, service_endpoint_policy_definition_name, api_version, subscription_id) -> web.Response:
    """service_endpoint_policy_definitions_delete

    Deletes the specified ServiceEndpoint policy definitions.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the Service Endpoint Policy.
    :type service_endpoint_policy_name: str
    :param service_endpoint_policy_definition_name: The name of the service endpoint policy definition.
    :type service_endpoint_policy_definition_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def service_endpoint_policy_definitions_list_by_resource_group(request: web.Request, resource_group_name, service_endpoint_policy_name, api_version, subscription_id) -> web.Response:
    """service_endpoint_policy_definitions_list_by_resource_group

    Gets all service endpoint policy definitions in a service end point policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy name.
    :type service_endpoint_policy_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
