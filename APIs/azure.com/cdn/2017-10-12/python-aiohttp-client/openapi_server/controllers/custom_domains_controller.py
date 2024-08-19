from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_domain import CustomDomain
from openapi_server.models.custom_domain_https_parameters import CustomDomainHttpsParameters
from openapi_server.models.custom_domain_list_result import CustomDomainListResult
from openapi_server.models.custom_domain_parameters import CustomDomainParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def custom_domains_create(request: web.Request, resource_group_name, profile_name, endpoint_name, custom_domain_name, subscription_id, api_version, custom_domain_properties) -> web.Response:
    """custom_domains_create

    Creates a new custom domain within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param custom_domain_name: Name of the custom domain within an endpoint.
    :type custom_domain_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param custom_domain_properties: Properties required to create a new custom domain.
    :type custom_domain_properties: dict | bytes

    """
    custom_domain_properties = CustomDomainParameters.from_dict(custom_domain_properties)
    return web.Response(status=200)


async def custom_domains_delete(request: web.Request, resource_group_name, profile_name, endpoint_name, custom_domain_name, subscription_id, api_version) -> web.Response:
    """custom_domains_delete

    Deletes an existing custom domain within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param custom_domain_name: Name of the custom domain within an endpoint.
    :type custom_domain_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_domains_disable_custom_https(request: web.Request, resource_group_name, profile_name, endpoint_name, custom_domain_name, subscription_id, api_version) -> web.Response:
    """custom_domains_disable_custom_https

    Disable https delivery of the custom domain.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param custom_domain_name: Name of the custom domain within an endpoint.
    :type custom_domain_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_domains_enable_custom_https(request: web.Request, resource_group_name, profile_name, endpoint_name, custom_domain_name, subscription_id, api_version, custom_domain_https_parameters=None) -> web.Response:
    """custom_domains_enable_custom_https

    Enable https delivery of the custom domain.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param custom_domain_name: Name of the custom domain within an endpoint.
    :type custom_domain_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param custom_domain_https_parameters: The configuration specifying how to enable HTTPS for the custom domain - using CDN managed certificate or user&#39;s own certificate. If not specified, enabling ssl uses CDN managed certificate by default.
    :type custom_domain_https_parameters: dict | bytes

    """
    custom_domain_https_parameters = CustomDomainHttpsParameters.from_dict(custom_domain_https_parameters)
    return web.Response(status=200)


async def custom_domains_get(request: web.Request, resource_group_name, profile_name, endpoint_name, custom_domain_name, subscription_id, api_version) -> web.Response:
    """custom_domains_get

    Gets an existing custom domain within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param custom_domain_name: Name of the custom domain within an endpoint.
    :type custom_domain_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_domains_list_by_endpoint(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """custom_domains_list_by_endpoint

    Lists all of the existing custom domains within an endpoint.

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
