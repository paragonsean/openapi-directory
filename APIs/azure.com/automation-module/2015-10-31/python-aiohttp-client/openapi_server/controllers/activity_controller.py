from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity import Activity
from openapi_server.models.activity_list_result import ActivityListResult
from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse
from openapi_server import util


async def activity_get(request: web.Request, resource_group_name, automation_account_name, module_name, activity_name, subscription_id, api_version) -> web.Response:
    """activity_get

    Retrieve the activity in the module identified by module name and activity name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The name of module.
    :type module_name: str
    :param activity_name: The name of activity.
    :type activity_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def activity_list_by_module(request: web.Request, resource_group_name, automation_account_name, module_name, subscription_id, api_version) -> web.Response:
    """activity_list_by_module

    Retrieve a list of activities in the module identified by module name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The name of module.
    :type module_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
