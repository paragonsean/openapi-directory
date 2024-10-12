from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.log_analytics_query_pack_query import LogAnalyticsQueryPackQuery
from openapi_server.models.log_analytics_query_pack_query_list_result import LogAnalyticsQueryPackQueryListResult
from openapi_server.models.log_analytics_query_pack_query_search_properties import LogAnalyticsQueryPackQuerySearchProperties
from openapi_server import util


async def queries_delete(request: web.Request, subscription_id, resource_group_name, query_pack_name, query_id, api_version) -> web.Response:
    """queries_delete

    Deletes a specific Query defined within an Log Analytics QueryPack.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param query_id: The id of a specific query defined in the Log Analytics QueryPack
    :type query_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def queries_get(request: web.Request, subscription_id, resource_group_name, query_pack_name, query_id, api_version) -> web.Response:
    """queries_get

    Gets a specific Log Analytics Query defined within a Log Analytics QueryPack.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param query_id: The id of a specific query defined in the Log Analytics QueryPack
    :type query_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def queries_list(request: web.Request, subscription_id, resource_group_name, query_pack_name, api_version, top=None, include_body=None, skip_token=None) -> web.Response:
    """queries_list

    Gets a list of Queries defined within a Log Analytics QueryPack.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param top: Maximum items returned in page.
    :type top: int
    :param include_body: Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
    :type include_body: bool
    :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
    :type skip_token: str

    """
    return web.Response(status=200)


async def queries_put(request: web.Request, subscription_id, resource_group_name, query_pack_name, query_id, api_version, query_payload) -> web.Response:
    """queries_put

    Adds or Updates a specific Query within a Log Analytics QueryPack.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param query_id: The id of a specific query defined in the Log Analytics QueryPack
    :type query_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param query_payload: Properties that need to be specified to create a new query and add it to a Log Analytics QueryPack.
    :type query_payload: dict | bytes

    """
    query_payload = LogAnalyticsQueryPackQuery.from_dict(query_payload)
    return web.Response(status=200)


async def queries_search(request: web.Request, subscription_id, resource_group_name, query_pack_name, api_version, query_search_properties, top=None, include_body=None, skip_token=None) -> web.Response:
    """queries_search

    Search a list of Queries defined within a Log Analytics QueryPack according to given search properties.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param query_pack_name: The name of the Log Analytics QueryPack resource.
    :type query_pack_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param query_search_properties: Properties by which to search queries in the given Log Analytics QueryPack.
    :type query_search_properties: dict | bytes
    :param top: Maximum items returned in page.
    :type top: int
    :param include_body: Flag indicating whether or not to return the body of each applicable query. If false, only return the query information.
    :type include_body: bool
    :param skip_token: Base64 encoded token used to fetch the next page of items. Default is null.
    :type skip_token: str

    """
    query_search_properties = LogAnalyticsQueryPackQuerySearchProperties.from_dict(query_search_properties)
    return web.Response(status=200)
