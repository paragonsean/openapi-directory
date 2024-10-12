from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.impacted_resource_list_result import ImpactedResourceListResult
from openapi_server import util


async def impacted_resources_list_by_subscription_id(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """impacted_resources_list_by_subscription_id

    Lists the current availability status for impacted resources in the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN
    :type filter: str

    """
    return web.Response(status=200)
