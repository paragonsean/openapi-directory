from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_list_by_service_default_response import GroupListByServiceDefaultResponse
from openapi_server.models.group_user_create200_response import GroupUserCreate200Response
from openapi_server.models.group_user_list200_response import GroupUserList200Response
from openapi_server import util


async def group_user_check_entity_exists(request: web.Request, resource_group_name, service_name, group_id, user_id, api_version, subscription_id) -> web.Response:
    """group_user_check_entity_exists

    Checks that user entity specified by identifier is associated with the group entity.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def group_user_create(request: web.Request, resource_group_name, service_name, group_id, user_id, api_version, subscription_id) -> web.Response:
    """group_user_create

    Add existing user to existing group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def group_user_delete(request: web.Request, resource_group_name, service_name, group_id, user_id, api_version, subscription_id) -> web.Response:
    """group_user_delete

    Remove existing user from existing group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param user_id: User identifier. Must be unique in the current API Management service instance.
    :type user_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def group_user_list(request: web.Request, resource_group_name, service_name, group_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """group_user_list

    Lists a collection of user entities associated with the group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param group_id: Group identifier. Must be unique in the current API Management service instance.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| firstName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| lastName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| email | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| registrationDate | filter | ge, le, eq, ne, gt, lt |     | &lt;/br&gt;| note | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
