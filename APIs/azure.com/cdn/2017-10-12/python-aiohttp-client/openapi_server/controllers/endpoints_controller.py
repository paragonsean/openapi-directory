from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint import Endpoint
from openapi_server.models.endpoint_list_result import EndpointListResult
from openapi_server.models.endpoint_update_parameters import EndpointUpdateParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.load_parameters import LoadParameters
from openapi_server.models.purge_parameters import PurgeParameters
from openapi_server.models.resource_usage_list_result import ResourceUsageListResult
from openapi_server.models.validate_custom_domain_input import ValidateCustomDomainInput
from openapi_server.models.validate_custom_domain_output import ValidateCustomDomainOutput
from openapi_server import util


async def endpoints_create(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version, endpoint) -> web.Response:
    """endpoints_create

    Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param endpoint: Endpoint properties
    :type endpoint: dict | bytes

    """
    endpoint = Endpoint.from_dict(endpoint)
    return web.Response(status=200)


async def endpoints_delete(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """endpoints_delete

    Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_get(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """endpoints_get

    Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_list_by_profile(request: web.Request, resource_group_name, profile_name, subscription_id, api_version) -> web.Response:
    """endpoints_list_by_profile

    Lists existing CDN endpoints.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_list_resource_usage(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """endpoints_list_resource_usage

    Checks the quota and usage of geo filters and custom domains under the given endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_load_content(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version, content_file_paths) -> web.Response:
    """endpoints_load_content

    Pre-loads a content to CDN. Available for Verizon Profiles.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param content_file_paths: The path to the content to be loaded. Path should be a full URL, e.g. ‘/pictures/city.png&#39; which loads a single file 
    :type content_file_paths: dict | bytes

    """
    content_file_paths = LoadParameters.from_dict(content_file_paths)
    return web.Response(status=200)


async def endpoints_purge_content(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version, content_file_paths) -> web.Response:
    """endpoints_purge_content

    Removes a content from CDN.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param content_file_paths: The path to the content to be purged. Path can be a full URL, e.g. &#39;/pictures/city.png&#39; which removes a single file, or a directory with a wildcard, e.g. &#39;/pictures/*&#39; which removes all folders and files in the directory.
    :type content_file_paths: dict | bytes

    """
    content_file_paths = PurgeParameters.from_dict(content_file_paths)
    return web.Response(status=200)


async def endpoints_start(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """endpoints_start

    Starts an existing CDN endpoint that is on a stopped state.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_stop(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """endpoints_stop

    Stops an existing running CDN endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def endpoints_update(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version, endpoint_update_properties) -> web.Response:
    """endpoints_update

    Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags and Origin HostHeader can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update custom domains, use the Update Custom Domain operation.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param endpoint_update_properties: Endpoint update properties
    :type endpoint_update_properties: dict | bytes

    """
    endpoint_update_properties = EndpointUpdateParameters.from_dict(endpoint_update_properties)
    return web.Response(status=200)


async def endpoints_validate_custom_domain(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version, custom_domain_properties) -> web.Response:
    """endpoints_validate_custom_domain

    Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param custom_domain_properties: Custom domain to be validated.
    :type custom_domain_properties: dict | bytes

    """
    custom_domain_properties = ValidateCustomDomainInput.from_dict(custom_domain_properties)
    return web.Response(status=200)
