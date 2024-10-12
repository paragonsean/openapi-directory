from typing import List, Dict
from aiohttp import web

from openapi_server.models.backend_get200_response import BackendGet200Response
from openapi_server.models.backend_list_by_service200_response import BackendListByService200Response
from openapi_server.models.backend_list_by_service_default_response import BackendListByServiceDefaultResponse
from openapi_server.models.backend_update_request import BackendUpdateRequest
from openapi_server import util


async def backend_create_or_update(request: web.Request, resource_group_name, service_name, backend_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """backend_create_or_update

    Creates or Updates a backend.

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
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = BackendGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def backend_delete(request: web.Request, resource_group_name, service_name, backend_id, if_match, api_version, subscription_id) -> web.Response:
    """backend_delete

    Deletes the specified backend.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param backend_id: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :type backend_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def backend_get(request: web.Request, resource_group_name, service_name, backend_id, api_version, subscription_id) -> web.Response:
    """backend_get

    Gets the details of the backend specified by its identifier.

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

    """
    return web.Response(status=200)


async def backend_get_entity_tag(request: web.Request, resource_group_name, service_name, backend_id, api_version, subscription_id) -> web.Response:
    """backend_get_entity_tag

    Gets the entity state (Etag) version of the backend specified by its identifier.

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

    """
    return web.Response(status=200)


async def backend_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """backend_list_by_service

    Lists a collection of backends in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| title | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| url | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def backend_update(request: web.Request, resource_group_name, service_name, backend_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """backend_update

    Updates an existing backend.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param backend_id: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :type backend_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = BackendUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
