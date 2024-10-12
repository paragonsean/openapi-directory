from typing import List, Dict
from aiohttp import web

from openapi_server.models.bgp_service_community_list_result import BgpServiceCommunityListResult
from openapi_server import util


async def bgp_service_communities_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """bgp_service_communities_list

    Gets all the available bgp service communities.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
