from typing import List, Dict
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.dedicated_cloud_service import DedicatedCloudService
from openapi_server.models.dedicated_cloud_service_list_response import DedicatedCloudServiceListResponse
from openapi_server.models.patch_payload import PatchPayload
from openapi_server import util


async def dedicated_cloud_services_create_or_update(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_service_name, api_version, dedicated_cloud_service_request) -> web.Response:
    """Implements dedicated cloud service PUT method

    Create dedicate cloud service

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_service_name: dedicated cloud Service name
    :type dedicated_cloud_service_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param dedicated_cloud_service_request: Create Dedicated Cloud Service request
    :type dedicated_cloud_service_request: dict | bytes

    """
    dedicated_cloud_service_request = DedicatedCloudService.from_dict(dedicated_cloud_service_request)
    return web.Response(status=200)


async def dedicated_cloud_services_delete(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_service_name, api_version) -> web.Response:
    """Implements dedicatedCloudService DELETE method

    Delete dedicate cloud service

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_service_name: dedicated cloud service name
    :type dedicated_cloud_service_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dedicated_cloud_services_get(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_service_name, api_version) -> web.Response:
    """Implements dedicatedCloudService GET method

    Returns Dedicate Cloud Service

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_service_name: dedicated cloud Service name
    :type dedicated_cloud_service_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def dedicated_cloud_services_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list of dedicatedCloudService objects within RG method

    Returns list of dedicated cloud services within a resource group

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def dedicated_cloud_services_list_by_subscription(request: web.Request, subscription_id, api_version, filter=None, top=None, skip_token=None) -> web.Response:
    """Implements list of dedicatedCloudService objects within subscription method

    Returns list of dedicated cloud services within a subscription

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the list operation
    :type filter: str
    :param top: The maximum number of record sets to return
    :type top: int
    :param skip_token: to be used by nextLink implementation
    :type skip_token: str

    """
    return web.Response(status=200)


async def dedicated_cloud_services_update(request: web.Request, subscription_id, resource_group_name, dedicated_cloud_service_name, api_version, dedicated_cloud_service_request) -> web.Response:
    """Implements dedicatedCloudService PATCH method

    Patch dedicated cloud service&#39;s properties

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group
    :type resource_group_name: str
    :param dedicated_cloud_service_name: dedicated cloud service name
    :type dedicated_cloud_service_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param dedicated_cloud_service_request: Patch Dedicated Cloud Service request
    :type dedicated_cloud_service_request: dict | bytes

    """
    dedicated_cloud_service_request = PatchPayload.from_dict(dedicated_cloud_service_request)
    return web.Response(status=200)
