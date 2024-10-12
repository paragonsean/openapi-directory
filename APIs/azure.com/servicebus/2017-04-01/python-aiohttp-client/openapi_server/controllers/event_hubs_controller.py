from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.event_hub_list_result import EventHubListResult
from openapi_server import util


async def event_hubs_list_by_namespace(request: web.Request, resource_group_name, namespace_name, api_version, subscription_id) -> web.Response:
    """event_hubs_list_by_namespace

    Gets all the Event Hubs in a service bus Namespace.

    :param resource_group_name: Name of the Resource group within the Azure subscription.
    :type resource_group_name: str
    :param namespace_name: The namespace name
    :type namespace_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
