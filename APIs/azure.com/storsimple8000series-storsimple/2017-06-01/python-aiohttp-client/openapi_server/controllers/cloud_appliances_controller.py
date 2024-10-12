from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_appliance import CloudAppliance
from openapi_server.models.cloud_appliance_configuration_list import CloudApplianceConfigurationList
from openapi_server import util


async def cloud_appliances_list_supported_configurations(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """cloud_appliances_list_supported_configurations

    Lists supported cloud appliance models and supported configurations.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def cloud_appliances_provision(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """cloud_appliances_provision

    Provisions cloud appliance.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The cloud appliance
    :type parameters: dict | bytes

    """
    parameters = CloudAppliance.from_dict(parameters)
    return web.Response(status=200)
