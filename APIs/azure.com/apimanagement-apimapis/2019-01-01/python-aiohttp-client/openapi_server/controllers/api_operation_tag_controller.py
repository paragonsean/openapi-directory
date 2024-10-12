from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.tag_get_by_operation200_response import TagGetByOperation200Response
from openapi_server.models.tag_list_by_operation200_response import TagListByOperation200Response
from openapi_server import util


async def tag_assign_to_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_assign_to_operation

    Assign tag to the Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_detach_from_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_detach_from_operation

    Detach the tag from the Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_get_by_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_get_by_operation

    Get tag associated with the Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_get_entity_state_by_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_get_entity_state_by_operation

    Gets the entity state version of the tag specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_list_by_operation(request: web.Request, resource_group_name, service_name, api_id, operation_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """tag_list_by_operation

    Lists all Tags associated with the Operation.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
    :type operation_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
