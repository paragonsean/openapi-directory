from typing import List, Dict
from aiohttp import web

from openapi_server.models.resource_link import ResourceLink
from openapi_server.models.resource_link_result import ResourceLinkResult
from openapi_server import util


async def resource_links_create_or_update(request: web.Request, link_id, api_version, parameters) -> web.Response:
    """resource_links_create_or_update

    Creates or updates a resource link between the specified resources.

    :param link_id: The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    :type link_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param parameters: Parameters for creating or updating a resource link.
    :type parameters: dict | bytes

    """
    parameters = ResourceLink.from_dict(parameters)
    return web.Response(status=200)


async def resource_links_delete(request: web.Request, link_id, api_version) -> web.Response:
    """resource_links_delete

    Deletes a resource link with the specified ID.

    :param link_id: The fully qualified ID of the resource link. Use the format, /subscriptions/{subscription-id}/resourceGroups/{resource-group-name}/{provider-namespace}/{resource-type}/{resource-name}/Microsoft.Resources/links/{link-name}. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    :type link_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_links_get(request: web.Request, link_id, api_version) -> web.Response:
    """resource_links_get

    Gets a resource link with the specified ID.

    :param link_id: The fully qualified Id of the resource link. For example, /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup/Microsoft.Web/sites/mySite/Microsoft.Resources/links/myLink
    :type link_id: str
    :param api_version: The API version to use for the operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def resource_links_list_at_source_scope(request: web.Request, scope, api_version, filter=None) -> web.Response:
    """resource_links_list_at_source_scope

    Gets a list of resource links at and below the specified source scope.

    :param scope: The fully qualified ID of the scope for getting the resource links. For example, to list resource links at and under a resource group, set the scope to /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myGroup.
    :type scope: str
    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param filter: The filter to apply when getting resource links. To get links only at the specified scope (not below the scope), use Filter.atScope().
    :type filter: str

    """
    return web.Response(status=200)


async def resource_links_list_at_subscription(request: web.Request, api_version, subscription_id, filter=None) -> web.Response:
    """resource_links_list_at_subscription

    Gets all the linked resources for the subscription.

    :param api_version: The API version to use for the operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param filter: The filter to apply on the list resource links operation. The supported filter for list resource links is targetId. For example, $filter&#x3D;targetId eq {value}
    :type filter: str

    """
    return web.Response(status=200)
