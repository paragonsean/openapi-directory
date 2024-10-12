from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_status import AvailabilityStatus
from openapi_server.models.availability_status_list_result import AvailabilityStatusListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def child_availability_statuses_get_by_resource(request: web.Request, resource_uri, api_version, filter=None, expand=None) -> web.Response:
    """child_availability_statuses_get_by_resource

    Gets current availability status for a single resource

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str
    :param expand: Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response.
    :type expand: str

    """
    return web.Response(status=200)


async def child_availability_statuses_list(request: web.Request, resource_uri, api_version, filter=None, expand=None) -> web.Response:
    """child_availability_statuses_list

    Lists the historical availability statuses for a single child resource. Use the nextLink property in the response to get the next page of availability status

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str
    :param expand: Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response.
    :type expand: str

    """
    return web.Response(status=200)
