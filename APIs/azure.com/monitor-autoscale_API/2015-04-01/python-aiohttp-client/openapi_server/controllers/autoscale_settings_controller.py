from typing import List, Dict
from aiohttp import web

from openapi_server.models.autoscale_setting_resource import AutoscaleSettingResource
from openapi_server.models.autoscale_setting_resource_collection import AutoscaleSettingResourceCollection
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def autoscale_settings_create_or_update(request: web.Request, resource_group_name, autoscale_setting_name, api_version, subscription_id, parameters) -> web.Response:
    """autoscale_settings_create_or_update

    Creates or updates an autoscale setting.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param autoscale_setting_name: The autoscale setting name.
    :type autoscale_setting_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str
    :param parameters: Parameters supplied to the operation.
    :type parameters: dict | bytes

    """
    parameters = AutoscaleSettingResource.from_dict(parameters)
    return web.Response(status=200)


async def autoscale_settings_delete(request: web.Request, resource_group_name, autoscale_setting_name, api_version, subscription_id) -> web.Response:
    """autoscale_settings_delete

    Deletes and autoscale setting

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param autoscale_setting_name: The autoscale setting name.
    :type autoscale_setting_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def autoscale_settings_get(request: web.Request, resource_group_name, autoscale_setting_name, api_version, subscription_id) -> web.Response:
    """autoscale_settings_get

    Gets an autoscale setting

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param autoscale_setting_name: The autoscale setting name.
    :type autoscale_setting_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def autoscale_settings_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """autoscale_settings_list_by_resource_group

    Lists the autoscale settings for a resource group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def autoscale_settings_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """autoscale_settings_list_by_subscription

    Lists the autoscale settings for a subscription

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: The Azure subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
