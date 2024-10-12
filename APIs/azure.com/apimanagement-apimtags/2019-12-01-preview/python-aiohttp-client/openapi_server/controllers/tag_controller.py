from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_create_or_update_request import TagCreateOrUpdateRequest
from openapi_server.models.tag_get200_response import TagGet200Response
from openapi_server.models.tag_list_by_service200_response import TagListByService200Response
from openapi_server.models.tag_list_by_service_default_response import TagListByServiceDefaultResponse
from openapi_server import util


async def tag_create_or_update(request: web.Request, resource_group_name, service_name, tag_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """tag_create_or_update

    Creates a tag.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
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
    parameters = TagCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)


async def tag_delete(request: web.Request, resource_group_name, service_name, tag_id, if_match, api_version, subscription_id) -> web.Response:
    """tag_delete

    Deletes specific tag of the API Management service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
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


async def tag_get(request: web.Request, resource_group_name, service_name, tag_id, api_version, subscription_id) -> web.Response:
    """tag_get

    Gets the details of the tag specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_get_entity_state(request: web.Request, resource_group_name, service_name, tag_id, api_version, subscription_id) -> web.Response:
    """tag_get_entity_state

    Gets the entity state version of the tag specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def tag_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, scope=None) -> web.Response:
    """tag_list_by_service

    Lists a collection of tags defined within a service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param scope: Scope like &#39;apis&#39;, &#39;products&#39; or &#39;apis/{apiId}
    :type scope: str

    """
    return web.Response(status=200)


async def tag_update(request: web.Request, resource_group_name, service_name, tag_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """tag_update

    Updates the details of the tag specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param tag_id: Tag identifier. Must be unique in the current API Management service instance.
    :type tag_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = TagCreateOrUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
