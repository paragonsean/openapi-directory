from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_groups_list_by_users200_response import UserGroupsListByUsers200Response
from openapi_server.models.users_list_by_service_default_response import UsersListByServiceDefaultResponse
from openapi_server import util


async def user_groups_list_by_users(request: web.Request, resource_group_name, service_name, uid, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """user_groups_list_by_users

    Lists all user groups.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param uid: User identifier. Must be unique in the current API Management service instance.
    :type uid: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
