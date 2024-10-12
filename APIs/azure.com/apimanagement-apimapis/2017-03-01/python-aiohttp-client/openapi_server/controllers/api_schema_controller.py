from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.schema_collection import SchemaCollection
from openapi_server.models.schema_contract import SchemaContract
from openapi_server import util


async def api_schema_create_or_update(request: web.Request, resource_group_name, service_name, api_id, schema_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_schema_create_or_update

    Creates or updates schema configuration for the API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :type schema_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The schema contents to apply.
    :type parameters: dict | bytes
    :param if_match: The entity state (Etag) version of the Api Schema to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str

    """
    parameters = SchemaContract.from_dict(parameters)
    return web.Response(status=200)


async def api_schema_delete(request: web.Request, resource_group_name, service_name, api_id, schema_id, if_match, api_version, subscription_id) -> web.Response:
    """api_schema_delete

    Deletes the schema configuration at the Api.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :type schema_id: str
    :param if_match: The entity state (Etag) version of the Api schema to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_schema_get(request: web.Request, resource_group_name, service_name, api_id, schema_id, api_version, subscription_id) -> web.Response:
    """api_schema_get

    Get the schema configuration at the API level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :type schema_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_schema_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, schema_id, api_version, subscription_id) -> web.Response:
    """api_schema_get_entity_tag

    Gets the entity state (Etag) version of the schema specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param schema_id: Schema identifier within an API. Must be unique in the current API Management service instance.
    :type schema_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_schema_list_by_api(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id) -> web.Response:
    """api_schema_list_by_api

    Get the schema configuration at the API level.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
