from typing import List, Dict
from aiohttp import web

from openapi_server.models.usages_list_result import UsagesListResult
from openapi_server import util


async def usages_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """usages_list

    Lists compute usages for a subscription.

    :param location: The location where resource usage is queried.
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
