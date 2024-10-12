from typing import List, Dict
from aiohttp import web

from openapi_server.models.widget_type_list_result import WidgetTypeListResult
from openapi_server.models.widget_type_resource_format import WidgetTypeResourceFormat
from openapi_server import util


async def widget_types_get(request: web.Request, resource_group_name, hub_name, widget_type_name, api_version, subscription_id) -> web.Response:
    """widget_types_get

    Gets a widget type in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param widget_type_name: The name of the widget type.
    :type widget_type_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def widget_types_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """widget_types_list_by_hub

    Gets all available widget types in the specified hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
