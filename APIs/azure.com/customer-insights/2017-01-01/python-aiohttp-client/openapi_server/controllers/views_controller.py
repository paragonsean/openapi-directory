from typing import List, Dict
from aiohttp import web

from openapi_server.models.view_list_result import ViewListResult
from openapi_server.models.view_resource_format import ViewResourceFormat
from openapi_server import util


async def views_create_or_update(request: web.Request, resource_group_name, hub_name, view_name, api_version, subscription_id, parameters) -> web.Response:
    """views_create_or_update

    Creates a view or updates an existing view in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param view_name: The name of the view.
    :type view_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the CreateOrUpdate View operation.
    :type parameters: dict | bytes

    """
    parameters = ViewResourceFormat.from_dict(parameters)
    return web.Response(status=200)


async def views_delete(request: web.Request, resource_group_name, hub_name, view_name, api_version, subscription_id, user_id) -> web.Response:
    """views_delete

    Deletes a view in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param view_name: The name of the view.
    :type view_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param user_id: The user ID. Use * to retrieve hub level view.
    :type user_id: str

    """
    return web.Response(status=200)


async def views_get(request: web.Request, resource_group_name, hub_name, view_name, api_version, subscription_id, user_id) -> web.Response:
    """views_get

    Gets a view in the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param view_name: The name of the view.
    :type view_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param user_id: The user ID. Use * to retrieve hub level view.
    :type user_id: str

    """
    return web.Response(status=200)


async def views_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id, user_id) -> web.Response:
    """views_list_by_hub

    Gets all available views for given user in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param user_id: The user ID. Use * to retrieve hub level views.
    :type user_id: str

    """
    return web.Response(status=200)
