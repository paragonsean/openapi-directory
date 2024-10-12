from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_endpoint_policy_definition import ServiceEndpointPolicyDefinition
from openapi_server import util


async def service_endpoint_policy_definitions_create_or_update(request: web.Request, resource_group_name, service_endpoint_policy_name, service_endpoint_policy_definition_name, api_version, subscription_id, service_endpoint_policy_definitions) -> web.Response:
    """service_endpoint_policy_definitions_create_or_update

    Creates or updates a service endpoint policy definition in the specified service endpoint policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy.
    :type service_endpoint_policy_name: str
    :param service_endpoint_policy_definition_name: The name of the service endpoint policy definition name.
    :type service_endpoint_policy_definition_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param service_endpoint_policy_definitions: Parameters supplied to the create or update service endpoint policy operation.
    :type service_endpoint_policy_definitions: dict | bytes

    """
    service_endpoint_policy_definitions = ServiceEndpointPolicyDefinition.from_dict(service_endpoint_policy_definitions)
    return web.Response(status=200)


async def service_endpoint_policy_definitions_get(request: web.Request, resource_group_name, service_endpoint_policy_name, service_endpoint_policy_definition_name, api_version, subscription_id) -> web.Response:
    """service_endpoint_policy_definitions_get

    Get the specified service endpoint policy definitions from service endpoint policy.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_endpoint_policy_name: The name of the service endpoint policy name.
    :type service_endpoint_policy_name: str
    :param service_endpoint_policy_definition_name: The name of the service endpoint policy definition name.
    :type service_endpoint_policy_definition_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
