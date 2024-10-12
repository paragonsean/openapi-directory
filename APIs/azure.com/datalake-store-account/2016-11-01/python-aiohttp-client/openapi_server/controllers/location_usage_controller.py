from typing import List, Dict
from aiohttp import web

from openapi_server.models.usage_list_result import UsageListResult
from openapi_server import util


async def locations_get_usage(request: web.Request, api_version, subscription_id, location) -> web.Response:
    """locations_get_usage

    Gets the current usage count and the limit for the resources of the location under the subscription.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: The resource location without whitespace.
    :type location: str

    """
    return web.Response(status=200)
