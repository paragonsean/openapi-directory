from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_analytics_query_pack import LogAnalyticsQueryPack
from openapi_server.models.log_analytics_query_pack_list_result import LogAnalyticsQueryPackListResult
from openapi_server.models.tags_resource import TagsResource
from openapi_server import util


async def query_packs_create_or_update(request: web.Request, resource_group_name, api_version, subscription_id, query_pack_name, log_analytics_query_pack_payload) -> web.Response:
    """query_packs_create_or_update

    Creates (or updates) a Log Analytics QueryPack. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param log_analytics_query_pack_payload: Properties that need to be specified to create or update a Log Analytics QueryPack.
    :type log_analytics_query_pack_payload: dict | bytes

    """
    log_analytics_query_pack_payload = LogAnalyticsQueryPack.from_dict(log_analytics_query_pack_payload)
    return web.Response(status=200)


async def query_packs_delete(request: web.Request, resource_group_name, api_version, subscription_id, query_pack_name) -> web.Response:
    """query_packs_delete

    Deletes a Log Analytics QueryPack.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str

    """
    return web.Response(status=200)


async def query_packs_get(request: web.Request, resource_group_name, api_version, subscription_id, query_pack_name) -> web.Response:
    """query_packs_get

    Returns a Log Analytics QueryPack.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str

    """
    return web.Response(status=200)


async def query_packs_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """query_packs_list

    Gets a list of all Log Analytics QueryPacks within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def query_packs_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """query_packs_list_by_resource_group

    Gets a list of Log Analytics QueryPacks within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def query_packs_update_tags(request: web.Request, resource_group_name, api_version, subscription_id, query_pack_name, query_pack_tags) -> web.Response:
    """query_packs_update_tags

    Updates an existing QueryPack&#39;s tags. To update other fields use the CreateOrUpdate method.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param query_pack_tags: Updated tag information to set into the QueryPack instance.
    :type query_pack_tags: dict | bytes

    """
    query_pack_tags = TagsResource.from_dict(query_pack_tags)
    return web.Response(status=200)
