from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component_favorite import ApplicationInsightsComponentFavorite
from openapi_server import util


async def favorites_add(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, favorite_id, favorite_properties) -> web.Response:
    """favorites_add

    Adds a new favorites to an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param favorite_id: The Id of a specific favorite defined in the Application Insights component
    :type favorite_id: str
    :param favorite_properties: Properties that need to be specified to create a new favorite and add it to an Application Insights component.
    :type favorite_properties: dict | bytes

    """
    favorite_properties = ApplicationInsightsComponentFavorite.from_dict(favorite_properties)
    return web.Response(status=200)


async def favorites_delete(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, favorite_id) -> web.Response:
    """favorites_delete

    Remove a favorite that is associated to an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param favorite_id: The Id of a specific favorite defined in the Application Insights component
    :type favorite_id: str

    """
    return web.Response(status=200)


async def favorites_get(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, favorite_id) -> web.Response:
    """favorites_get

    Get a single favorite by its FavoriteId, defined within an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param favorite_id: The Id of a specific favorite defined in the Application Insights component
    :type favorite_id: str

    """
    return web.Response(status=200)


async def favorites_list(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, favorite_type=None, source_type=None, can_fetch_content=None, tags=None) -> web.Response:
    """favorites_list

    Gets a list of favorites defined within an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param favorite_type: The type of favorite. Value can be either shared or user.
    :type favorite_type: str
    :param source_type: Source type of favorite to return. When left out, the source type defaults to &#39;other&#39; (not present in this enum).
    :type source_type: str
    :param can_fetch_content: Flag indicating whether or not to return the full content for each applicable favorite. If false, only return summary content for favorites.
    :type can_fetch_content: bool
    :param tags: Tags that must be present on each favorite returned.
    :type tags: List[str]

    """
    return web.Response(status=200)


async def favorites_update(request: web.Request, resource_group_name, api_version, subscription_id, resource_name, favorite_id, favorite_properties) -> web.Response:
    """favorites_update

    Updates a favorite that has already been added to an Application Insights component.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param favorite_id: The Id of a specific favorite defined in the Application Insights component
    :type favorite_id: str
    :param favorite_properties: Properties that need to be specified to update the existing favorite.
    :type favorite_properties: dict | bytes

    """
    favorite_properties = ApplicationInsightsComponentFavorite.from_dict(favorite_properties)
    return web.Response(status=200)
