from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.origin_group import OriginGroup
from openapi_server.models.origin_group_list_result import OriginGroupListResult
from openapi_server.models.origin_group_update_parameters import OriginGroupUpdateParameters
from openapi_server import util


async def origin_groups_create(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_group_name, subscription_id, api_version, origin_group) -> web.Response:
    """origin_groups_create

    Creates a new origin group within the specified endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_group_name: Name of the origin group which is unique within the endpoint.
    :type origin_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param origin_group: Origin group properties
    :type origin_group: dict | bytes

    """
    origin_group = OriginGroup.from_dict(origin_group)
    return web.Response(status=200)


async def origin_groups_delete(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_group_name, subscription_id, api_version) -> web.Response:
    """origin_groups_delete

    Deletes an existing origin group within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_group_name: Name of the origin group which is unique within the endpoint.
    :type origin_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def origin_groups_get(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_group_name, subscription_id, api_version) -> web.Response:
    """origin_groups_get

    Gets an existing origin group within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_group_name: Name of the origin group which is unique within the endpoint.
    :type origin_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def origin_groups_list_by_endpoint(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """origin_groups_list_by_endpoint

    Lists all of the existing origin groups within an endpoint.

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


async def origin_groups_update(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_group_name, subscription_id, api_version, origin_group_update_properties) -> web.Response:
    """origin_groups_update

    Updates an existing origin group within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_group_name: Name of the origin group which is unique within the endpoint.
    :type origin_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param origin_group_update_properties: Origin group properties
    :type origin_group_update_properties: dict | bytes

    """
    origin_group_update_properties = OriginGroupUpdateParameters.from_dict(origin_group_update_properties)
    return web.Response(status=200)
