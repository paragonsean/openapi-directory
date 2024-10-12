from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_status_list_result import AvailabilityStatusListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def child_resources_list(request: web.Request, resource_uri, api_version, filter=None, expand=None) -> web.Response:
    """child_resources_list

    Lists the all the children and its current health status for a parent resource. Use the nextLink property in the response to get the next page of children current health

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support not nested parent resource type: /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str
    :param expand: Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response.
    :type expand: str

    """
    return web.Response(status=200)
