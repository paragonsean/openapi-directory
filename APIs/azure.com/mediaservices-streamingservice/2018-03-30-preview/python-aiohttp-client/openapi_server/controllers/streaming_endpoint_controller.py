from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_events_list_default_response import LiveEventsListDefaultResponse
from openapi_server.models.streaming_endpoint import StreamingEndpoint
from openapi_server import util


async def streaming_endpoints_update(request: web.Request, subscription_id, resource_group_name, account_name, streaming_endpoint_name, api_version, parameters) -> web.Response:
    """Update StreamingEndpoint

    Updates a existing StreamingEndpoint.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_endpoint_name: The name of the StreamingEndpoint.
    :type streaming_endpoint_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: StreamingEndpoint properties needed for creation.
    :type parameters: dict | bytes

    """
    parameters = StreamingEndpoint.from_dict(parameters)
    return web.Response(status=200)
