from typing import List, Dict
from aiohttp import web

from openapi_server.models.network_status_contract import NetworkStatusContract
from openapi_server.models.network_status_get_by_service_default_response import NetworkStatusGetByServiceDefaultResponse
from openapi_server import util


async def network_status_get_by_service(request: web.Request, subscription_id, resource_group_name, service_name, api_version) -> web.Response:
    """network_status_get_by_service

    Gets the Connectivity Status to the external resources on which the Api Management service depends from inside the Cloud Service. This also returns the DNS Servers as visible to the CloudService.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)
