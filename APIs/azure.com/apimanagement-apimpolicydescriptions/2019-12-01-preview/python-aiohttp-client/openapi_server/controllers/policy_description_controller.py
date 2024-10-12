from typing import List, Dict
from aiohttp import web

from openapi_server.models.policy_description_list_by_service200_response import PolicyDescriptionListByService200Response
from openapi_server.models.policy_description_list_by_service_default_response import PolicyDescriptionListByServiceDefaultResponse
from openapi_server import util


async def policy_description_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, scope=None) -> web.Response:
    """policy_description_list_by_service

    Lists all policy descriptions.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param scope: Policy scope.
    :type scope: str

    """
    return web.Response(status=200)
