from typing import List, Dict
from aiohttp import web

from openapi_server.models.backend_list_by_service_default_response import BackendListByServiceDefaultResponse
from openapi_server.models.backend_reconnect_request import BackendReconnectRequest
from openapi_server import util


async def backend_reconnect(request: web.Request, resource_group_name, service_name, backend_id, api_version, subscription_id, parameters=None) -> web.Response:
    """backend_reconnect

    Notifies the APIM proxy to create a new connection to the backend after the specified timeout. If no timeout was specified, timeout of 2 minutes is used.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param backend_id: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :type backend_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Reconnect request parameters.
    :type parameters: dict | bytes

    """
    parameters = BackendReconnectRequest.from_dict(parameters)
    return web.Response(status=200)
