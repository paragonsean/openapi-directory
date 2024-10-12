from typing import List, Dict
from aiohttp import web

from openapi_server.models.watcher import Watcher
from openapi_server.models.watcher_list_by_automation_account_default_response import WatcherListByAutomationAccountDefaultResponse
from openapi_server.models.watcher_list_result import WatcherListResult
from openapi_server.models.watcher_update_parameters import WatcherUpdateParameters
from openapi_server import util


async def watcher_create_or_update(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version, parameters) -> web.Response:
    """watcher_create_or_update

    Create the watcher identified by watcher name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for watcher.
    :type parameters: dict | bytes

    """
    parameters = Watcher.from_dict(parameters)
    return web.Response(status=200)


async def watcher_delete(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version) -> web.Response:
    """watcher_delete

    Delete the watcher by name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def watcher_get(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version) -> web.Response:
    """watcher_get

    Retrieve the watcher identified by watcher name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def watcher_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version, filter=None) -> web.Response:
    """watcher_list_by_automation_account

    Retrieve a list of watchers.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str

    """
    return web.Response(status=200)


async def watcher_start(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version) -> web.Response:
    """watcher_start

    Resume the watcher identified by watcher name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def watcher_stop(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version) -> web.Response:
    """watcher_stop

    Resume the watcher identified by watcher name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def watcher_update(request: web.Request, resource_group_name, automation_account_name, watcher_name, subscription_id, api_version, parameters) -> web.Response:
    """watcher_update

    Update the watcher identified by watcher name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param watcher_name: The watcher name.
    :type watcher_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The update parameters for watcher.
    :type parameters: dict | bytes

    """
    parameters = WatcherUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
