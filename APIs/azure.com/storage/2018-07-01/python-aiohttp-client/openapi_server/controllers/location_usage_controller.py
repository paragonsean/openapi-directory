from typing import List, Dict
from aiohttp import web

from openapi_server.models.usage_list_result import UsageListResult
from openapi_server import util


async def usages_list_by_location(request: web.Request, api_version, subscription_id, location) -> web.Response:
    """usages_list_by_location

    Gets the current usage count and the limit for the resources of the location under the subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param location: The location of the Azure Storage resource.
    :type location: str

    """
    return web.Response(status=200)
