from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.api_release_collection import ApiReleaseCollection
from openapi_server.models.api_release_contract import ApiReleaseContract
from openapi_server import util


async def api_release_create(request: web.Request, resource_group_name, service_name, api_version, subscription_id, api_id, release_id, parameters) -> web.Response:
    """api_release_create

    Creates a new Release for the API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :type release_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiReleaseContract.from_dict(parameters)
    return web.Response(status=200)


async def api_release_delete(request: web.Request, resource_group_name, service_name, api_version, subscription_id, api_id, release_id, if_match) -> web.Response:
    """api_release_delete

    Deletes the specified release in the API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :type release_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str

    """
    return web.Response(status=200)


async def api_release_get(request: web.Request, resource_group_name, service_name, api_version, subscription_id, api_id, release_id) -> web.Response:
    """api_release_get

    Returns the details of an API release.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :type release_id: str

    """
    return web.Response(status=200)


async def api_release_get_entity_tag(request: web.Request, resource_group_name, service_name, api_version, subscription_id, api_id, release_id) -> web.Response:
    """api_release_get_entity_tag

    Returns the etag of an API release.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :type release_id: str

    """
    return web.Response(status=200)


async def api_release_list(request: web.Request, resource_group_name, service_name, api_id, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """api_release_list

    Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters.

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
    :param filter: | Field | Supported operators    | Supported functions                         | |-------|------------------------|---------------------------------------------| | name  | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | |notes|ge le eq ne gt lt|substringof contains startswith endswith|
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)


async def api_release_update(request: web.Request, resource_group_name, service_name, api_version, subscription_id, api_id, release_id, if_match, parameters) -> web.Response:
    """api_release_update

    Updates the details of the release of the API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :type release_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param parameters: API Release Update parameters.
    :type parameters: dict | bytes

    """
    parameters = ApiReleaseContract.from_dict(parameters)
    return web.Response(status=200)
