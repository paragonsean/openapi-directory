from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_insights_component_analytics_item import ApplicationInsightsComponentAnalyticsItem
from openapi_server import util


async def analytics_items_delete(request: web.Request, subscription_id, resource_group_name, resource_name, scope_path, api_version, id=None, name=None) -> web.Response:
    """analytics_items_delete

    Deletes a specific Analytics Items defined within an Application Insights component.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param scope_path: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    :type scope_path: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param id: The Id of a specific item defined in the Application Insights component
    :type id: str
    :param name: The name of a specific item defined in the Application Insights component
    :type name: str

    """
    return web.Response(status=200)


async def analytics_items_get(request: web.Request, subscription_id, resource_group_name, resource_name, scope_path, api_version, id=None, name=None) -> web.Response:
    """analytics_items_get

    Gets a specific Analytics Items defined within an Application Insights component.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param scope_path: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    :type scope_path: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param id: The Id of a specific item defined in the Application Insights component
    :type id: str
    :param name: The name of a specific item defined in the Application Insights component
    :type name: str

    """
    return web.Response(status=200)


async def analytics_items_list(request: web.Request, subscription_id, resource_group_name, resource_name, scope_path, api_version, scope=None, type=None, include_content=None) -> web.Response:
    """analytics_items_list

    Gets a list of Analytics Items defined within an Application Insights component.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param scope_path: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    :type scope_path: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param scope: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    :type scope: str
    :param type: Enum indicating the type of the Analytics item.
    :type type: str
    :param include_content: Flag indicating whether or not to return the content of each applicable item. If false, only return the item information.
    :type include_content: bool

    """
    return web.Response(status=200)


async def analytics_items_put(request: web.Request, subscription_id, resource_group_name, resource_name, scope_path, api_version, item_properties, override_item=None) -> web.Response:
    """analytics_items_put

    Adds or Updates a specific Analytics Item within an Application Insights component.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param resource_name: The name of the Application Insights component resource.
    :type resource_name: str
    :param scope_path: Enum indicating if this item definition is owned by a specific user or is shared between all users with access to the Application Insights component.
    :type scope_path: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param item_properties: Properties that need to be specified to create a new item and add it to an Application Insights component.
    :type item_properties: dict | bytes
    :param override_item: Flag indicating whether or not to force save an item. This allows overriding an item if it already exists.
    :type override_item: bool

    """
    item_properties = ApplicationInsightsComponentAnalyticsItem.from_dict(item_properties)
    return web.Response(status=200)
