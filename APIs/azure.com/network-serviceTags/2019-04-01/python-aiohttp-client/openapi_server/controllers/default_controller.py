from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_tags_list_result import ServiceTagsListResult
from openapi_server import util


async def service_tags_list(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """service_tags_list

    Gets a list of service tag information resources.

    :param location: The location that will be used as a reference for version (not as a filter based on location, you will get the list of service tags with prefix details across all regions but limited to the cloud that your subscription belongs to).
    :type location: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
