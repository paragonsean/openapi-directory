from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_get_shared_access_token200_response import UserGetSharedAccessToken200Response
from openapi_server.models.user_get_shared_access_token_request import UserGetSharedAccessTokenRequest
from openapi_server.models.user_list_by_service_default_response import UserListByServiceDefaultResponse
from openapi_server import util


async def user_get_shared_access_token(request: web.Request, resource_group_name, service_name, user_id, api_version, subscription_id, parameters) -> web.Response:
    """user_get_shared_access_token

    Gets the Shared Access Authorization Token for the User.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create Authorization Token parameters.
    :type parameters: dict | bytes

    """
    parameters = UserGetSharedAccessTokenRequest.from_dict(parameters)
    return web.Response(status=200)
