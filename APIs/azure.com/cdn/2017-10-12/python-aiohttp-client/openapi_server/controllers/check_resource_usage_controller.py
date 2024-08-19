from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.resource_usage_list_result import ResourceUsageListResult
from openapi_server import util


async def resource_usage_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """resource_usage_list

    Check the quota and actual usage of the CDN profiles under the given subscription.

    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-04-02.
    :type api_version: str

    """
    return web.Response(status=200)
