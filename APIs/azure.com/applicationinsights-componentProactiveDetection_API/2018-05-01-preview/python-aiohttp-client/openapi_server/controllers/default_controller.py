from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component_proactive_detection_configuration import ApplicationInsightsComponentProactiveDetectionConfiguration
from openapi_server import util


async def proactive_detection_configurations_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, configuration_id) -> web.Response:
    """proactive_detection_configurations_get

    Get the ProactiveDetection configuration for this configuration id.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    :type configuration_id: str

    """
    return web.Response(status=200)


async def proactive_detection_configurations_list(request: web.Request, resource_group_name, api_version, subscription_id, resource_name) -> web.Response:
    """proactive_detection_configurations_list

    Gets a list of ProactiveDetection configurations of an Application Insights component.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str

    """
    return web.Response(status=200)


async def proactive_detection_configurations_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, configuration_id, proactive_detection_properties) -> web.Response:
    """proactive_detection_configurations_update

    Update the ProactiveDetection configuration for this configuration id.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    :type configuration_id: str
    :param proactive_detection_properties: Properties that need to be specified to update the ProactiveDetection configuration.
    :type proactive_detection_properties: dict | bytes

    """
    proactive_detection_properties = ApplicationInsightsComponentProactiveDetectionConfiguration.from_dict(proactive_detection_properties)
    return web.Response(status=200)
