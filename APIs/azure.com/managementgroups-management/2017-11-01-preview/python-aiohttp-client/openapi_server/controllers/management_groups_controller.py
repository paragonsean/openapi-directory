from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_management_group_request import CreateManagementGroupRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.management_group import ManagementGroup
from openapi_server.models.management_group_list_result import ManagementGroupListResult
from openapi_server import util


async def management_group_subscriptions_create(request: web.Request, group_id, subscription_id, api_version, cache_control=None) -> web.Response:
    """management_group_subscriptions_create

    Associates existing subscription with the management group. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)


async def management_group_subscriptions_delete(request: web.Request, group_id, subscription_id, api_version, cache_control=None) -> web.Response:
    """management_group_subscriptions_delete

    De-associates subscription from the management group. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param subscription_id: Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)


async def management_groups_create_or_update(request: web.Request, group_id, api_version, create_management_group_request, cache_control=None) -> web.Response:
    """management_groups_create_or_update

    Create or update a management group. If a management group is already created and a subsequent create request is issued with different properties, the management group properties will be updated. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param create_management_group_request: Management group creation parameters.
    :type create_management_group_request: dict | bytes
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    create_management_group_request = CreateManagementGroupRequest.from_dict(create_management_group_request)
    return web.Response(status=200)


async def management_groups_delete(request: web.Request, group_id, api_version, cache_control=None) -> web.Response:
    """management_groups_delete

    Delete management group. If a management group contains child resources, the request will fail. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)


async def management_groups_get(request: web.Request, group_id, api_version, expand=None, recurse=None, cache_control=None) -> web.Response:
    """management_groups_get

    Get the details of the management group. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param expand: The $expand&#x3D;children query string parameter allows clients to request inclusion of children in the response payload.
    :type expand: str
    :param recurse: The $recurse&#x3D;true query string parameter allows clients to request inclusion of entire hierarchy in the response payload.
    :type recurse: bool
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)


async def management_groups_list(request: web.Request, api_version, cache_control=None, skiptoken=None) -> web.Response:
    """management_groups_list

    List management groups for the authenticated user. 

    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str
    :param skiptoken: Page continuation token is only used if a previous operation returned a partial result.  If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls. 
    :type skiptoken: str

    """
    return web.Response(status=200)


async def management_groups_update(request: web.Request, group_id, api_version, create_management_group_request, cache_control=None) -> web.Response:
    """management_groups_update

    Update a management group. 

    :param group_id: Management Group ID.
    :type group_id: str
    :param api_version: Version of the API to be used with the client request. The current version is 2017-11-01-preview.
    :type api_version: str
    :param create_management_group_request: Management group creation parameters.
    :type create_management_group_request: dict | bytes
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    create_management_group_request = CreateManagementGroupRequest.from_dict(create_management_group_request)
    return web.Response(status=200)
