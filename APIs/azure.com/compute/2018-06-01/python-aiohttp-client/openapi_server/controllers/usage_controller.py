from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_usages_result import ListUsagesResult
from openapi_server import util


async def usage_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """usage_list

    Gets, for the specified location, the current compute resource usage information as well as the limits for compute resources under the subscription.

    :param location: The location for which resource usage is queried.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
