from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.events import Events
from openapi_server import util


async def events_list_by_single_resource(request: web.Request, resource_uri, api_version, filter=None, view=None) -> web.Response:
    """events_list_by_single_resource

    Lists current service health events for given resource.

    :param resource_uri: The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
    :type resource_uri: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str
    :param view: setting view&#x3D;full expands the article parameters
    :type view: str

    """
    return web.Response(status=200)


async def events_list_by_subscription_id(request: web.Request, api_version, subscription_id, filter=None, view=None) -> web.Response:
    """events_list_by_subscription_id

    Lists current service health events in the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str
    :param view: setting view&#x3D;full expands the article parameters
    :type view: str

    """
    return web.Response(status=200)
