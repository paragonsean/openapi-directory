from typing import List, Dict
from aiohttp import web

from openapi_server.models.module import Module
from openapi_server.models.module_list_result import ModuleListResult
from openapi_server.models.python2_package_list_by_automation_account_default_response import Python2PackageListByAutomationAccountDefaultResponse
from openapi_server.models.python_package_create_parameters import PythonPackageCreateParameters
from openapi_server.models.python_package_update_parameters import PythonPackageUpdateParameters
from openapi_server import util


async def python2_package_create_or_update(request: web.Request, resource_group_name, automation_account_name, package_name, subscription_id, api_version, parameters) -> web.Response:
    """python2_package_create_or_update

    Create or Update the python 2 package identified by package name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param package_name: The name of python package.
    :type package_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The create or update parameters for python package.
    :type parameters: dict | bytes

    """
    parameters = PythonPackageCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def python2_package_delete(request: web.Request, resource_group_name, automation_account_name, package_name, subscription_id, api_version) -> web.Response:
    """python2_package_delete

    Delete the python 2 package by name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param package_name: The python package name.
    :type package_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def python2_package_get(request: web.Request, resource_group_name, automation_account_name, package_name, subscription_id, api_version) -> web.Response:
    """python2_package_get

    Retrieve the python 2 package identified by package name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param package_name: The python package name.
    :type package_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def python2_package_list_by_automation_account(request: web.Request, resource_group_name, automation_account_name, subscription_id, api_version) -> web.Response:
    """python2_package_list_by_automation_account

    Retrieve a list of python 2 packages.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def python2_package_update(request: web.Request, resource_group_name, automation_account_name, package_name, subscription_id, api_version, parameters) -> web.Response:
    """python2_package_update

    Update the python 2 package identified by package name.

    :param resource_group_name: Name of an Azure Resource group.
    :type resource_group_name: str
    :param automation_account_name: The name of the automation account.
    :type automation_account_name: str
    :param package_name: The name of python package.
    :type package_name: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param parameters: The update parameters for python package.
    :type parameters: dict | bytes

    """
    parameters = PythonPackageUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
