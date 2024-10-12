from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_https_configuration import CustomHttpsConfiguration
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.front_door import FrontDoor
from openapi_server.models.front_door_list_result import FrontDoorListResult
from openapi_server.models.frontend_endpoint import FrontendEndpoint
from openapi_server.models.frontend_endpoints_list_result import FrontendEndpointsListResult
from openapi_server.models.purge_parameters import PurgeParameters
from openapi_server.models.validate_custom_domain_input import ValidateCustomDomainInput
from openapi_server.models.validate_custom_domain_output import ValidateCustomDomainOutput
from openapi_server import util


async def endpoints_purge_content(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version, content_file_paths) -> web.Response:
    """endpoints_purge_content

    Removes a content from Front Door.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param content_file_paths: The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/*&#39; which removes all folders and files in the directory.
    :type content_file_paths: dict | bytes

    """
    content_file_paths = PurgeParameters.from_dict(content_file_paths)
    return web.Response(status=200)


async def front_doors_create_or_update(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version, front_door_parameters) -> web.Response:
    """front_doors_create_or_update

    Creates a new Front Door with a Front Door name under the specified subscription and resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param front_door_parameters: Front Door properties needed to create a new Front Door.
    :type front_door_parameters: dict | bytes

    """
    front_door_parameters = FrontDoor.from_dict(front_door_parameters)
    return web.Response(status=200)


async def front_doors_delete(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version) -> web.Response:
    """front_doors_delete

    Deletes an existing Front Door with the specified parameters.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def front_doors_get(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version) -> web.Response:
    """front_doors_get

    Gets a Front Door with the specified Front Door name under the specified subscription and resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def front_doors_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """front_doors_list

    Lists all of the Front Doors within an Azure subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def front_doors_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """front_doors_list_by_resource_group

    Lists all of the Front Doors within a resource group under a subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def front_doors_validate_custom_domain(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version, custom_domain_properties) -> web.Response:
    """front_doors_validate_custom_domain

    Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param custom_domain_properties: Custom domain to be validated.
    :type custom_domain_properties: dict | bytes

    """
    custom_domain_properties = ValidateCustomDomainInput.from_dict(custom_domain_properties)
    return web.Response(status=200)


async def frontend_endpoints_disable_https(request: web.Request, subscription_id, resource_group_name, front_door_name, frontend_endpoint_name, api_version) -> web.Response:
    """frontend_endpoints_disable_https

    Disables a frontendEndpoint for HTTPS traffic

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front Door.
    :type frontend_endpoint_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def frontend_endpoints_enable_https(request: web.Request, subscription_id, resource_group_name, front_door_name, frontend_endpoint_name, api_version, custom_https_configuration) -> web.Response:
    """frontend_endpoints_enable_https

    Enables a frontendEndpoint for HTTPS traffic

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front Door.
    :type frontend_endpoint_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param custom_https_configuration: The configuration specifying how to enable HTTPS
    :type custom_https_configuration: dict | bytes

    """
    custom_https_configuration = CustomHttpsConfiguration.from_dict(custom_https_configuration)
    return web.Response(status=200)


async def frontend_endpoints_get(request: web.Request, subscription_id, resource_group_name, front_door_name, frontend_endpoint_name, api_version) -> web.Response:
    """frontend_endpoints_get

    Gets a Frontend endpoint with the specified name within the specified Front Door.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param frontend_endpoint_name: Name of the Frontend endpoint which is unique within the Front Door.
    :type frontend_endpoint_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def frontend_endpoints_list_by_front_door(request: web.Request, subscription_id, resource_group_name, front_door_name, api_version) -> web.Response:
    """frontend_endpoints_list_by_front_door

    Lists all of the frontend endpoints within a Front Door.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param front_door_name: Name of the Front Door which is globally unique.
    :type front_door_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)
