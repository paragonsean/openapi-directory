from typing import List, Dict
from aiohttp import web

from openapi_server.models.region_list_result import RegionListResult
from openapi_server import util


async def regions_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id) -> web.Response:
    """regions_list_by_service

    Lists all azure regions in which the service exists.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
