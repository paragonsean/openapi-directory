from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_create_or_update_request import ApiCreateOrUpdateRequest
from openapi_server.models.api_get200_response import ApiGet200Response
from openapi_server.models.api_list_by_service200_response import ApiListByService200Response
from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.api_update_request import ApiUpdateRequest
from openapi_server import util


async def api_create_or_update(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_create_or_update

    Creates new or updates existing specified API of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = ApiCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)


async def api_delete(request: web.Request, resource_group_name, service_name, api_id, if_match, api_version, subscription_id, delete_revisions=None) -> web.Response:
    """api_delete

    Deletes the specified API of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delete_revisions: Delete all revisions of the Api.
    :type delete_revisions: bool

    """
    return web.Response(status=200)


async def api_get(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id) -> web.Response:
    """api_get

    Gets the details of the API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id) -> web.Response:
    """api_get_entity_tag

    Gets the entity state (Etag) version of the API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, tags=None, expand_api_version_set=None) -> web.Response:
    """api_list_by_service

    Lists all APIs of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param tags: Include tags in the response.
    :type tags: str
    :param expand_api_version_set: Include full ApiVersionSet resource in response
    :type expand_api_version_set: bool

    """
    return web.Response(status=200)


async def api_update(request: web.Request, resource_group_name, service_name, api_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """api_update

    Updates the specified API of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: API Update Contract parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
