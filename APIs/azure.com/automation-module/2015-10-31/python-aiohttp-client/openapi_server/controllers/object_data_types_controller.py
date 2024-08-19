from typing import List, Dict
from aiohttp import web

from openapi_server.models.module_list_by_automation_account_default_response import ModuleListByAutomationAccountDefaultResponse
from openapi_server.models.type_field_list_result import TypeFieldListResult
from openapi_server import util


async def object_data_types_list_fields_by_module_and_type(request: web.Request, resource_group_name, automation_account_name, module_name, type_name, subscription_id, api_version) -> web.Response:
    """object_data_types_list_fields_by_module_and_type

    Retrieve a list of fields of a given type identified by module name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param module_name: The name of module.
    :type module_name: str
    :param type_name: The name of type.
    :type type_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def object_data_types_list_fields_by_type(request: web.Request, resource_group_name, automation_account_name, type_name, subscription_id, api_version) -> web.Response:
    """object_data_types_list_fields_by_type

    Retrieve a list of fields of a given type across all accessible modules.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param type_name: The name of type.
    :type type_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
