from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.origin import Origin
from openapi_server.models.origin_list_result import OriginListResult
from openapi_server.models.origin_update_parameters import OriginUpdateParameters
from openapi_server import util


async def origins_get(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_name, subscription_id, api_version) -> web.Response:
    """origins_get

    Gets an existing origin within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_name: Name of the origin which is unique within the endpoint.
    :type origin_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)


async def origins_list_by_endpoint(request: web.Request, resource_group_name, profile_name, endpoint_name, subscription_id, api_version) -> web.Response:
    """origins_list_by_endpoint

    Lists all of the existing origins within an endpoint.

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


async def origins_update(request: web.Request, resource_group_name, profile_name, endpoint_name, origin_name, subscription_id, api_version, origin_update_properties) -> web.Response:
    """origins_update

    Updates an existing origin within an endpoint.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param profile_name: Name of the CDN profile which is unique within the resource group.
    :type profile_name: str
    :param endpoint_name: Name of the endpoint under the profile which is unique globally.
    :type endpoint_name: str
    :param origin_name: Name of the origin which is unique within the endpoint.
    :type origin_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str
    :param origin_update_properties: Origin properties
    :type origin_update_properties: dict | bytes

    """
    origin_update_properties = OriginUpdateParameters.from_dict(origin_update_properties)
    return web.Response(status=200)
