from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_description_collection import TagDescriptionCollection
from openapi_server.models.tag_description_contract import TagDescriptionContract
from openapi_server.models.tag_description_create_parameters import TagDescriptionCreateParameters
from openapi_server.models.tag_list_by_operation_default_response import TagListByOperationDefaultResponse
from openapi_server import util


async def tag_description_create_or_update(request: web.Request, resource_group_name, service_name, api_id, tag_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """tag_description_create_or_update

    Create/Update tag description in scope of the Api.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = TagDescriptionCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def tag_description_delete(request: web.Request, resource_group_name, service_name, api_id, tag_id, if_match, api_version, subscription_id) -> web.Response:
    """tag_description_delete

    Delete tag description for the Api.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_description_get(request: web.Request, resource_group_name, service_name, api_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_description_get

    Get tag associated with the API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_description_get_entity_state(request: web.Request, resource_group_name, service_name, api_id, tag_id, api_version, subscription_id) -> web.Response:
    """tag_description_get_entity_state

    Gets the entity state version of the tag specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev&#x3D;n as a suffix where n is the revision number.
    :type api_id: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_description_list_by_api(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """tag_description_list_by_api

    Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations

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
    :param filter: | Field       | Supported operators    | Supported functions                         | |-------------|------------------------|---------------------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | | name        | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
