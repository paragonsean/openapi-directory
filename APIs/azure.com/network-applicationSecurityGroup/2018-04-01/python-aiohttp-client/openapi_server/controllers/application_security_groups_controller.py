from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_security_group import ApplicationSecurityGroup
from openapi_server.models.application_security_group_list_result import ApplicationSecurityGroupListResult
from openapi_server import util


async def application_security_groups_create_or_update(request: web.Request, resource_group_name, application_security_group_name, api_version, subscription_id, parameters) -> web.Response:
    """application_security_groups_create_or_update

    Creates or updates an application security group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_security_group_name: The name of the application security group.
    :type application_security_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update ApplicationSecurityGroup operation.
    :type parameters: dict | bytes

    """
    parameters = ApplicationSecurityGroup.from_dict(parameters)
    return web.Response(status=200)


async def application_security_groups_delete(request: web.Request, resource_group_name, application_security_group_name, api_version, subscription_id) -> web.Response:
    """application_security_groups_delete

    Deletes the specified application security group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_security_group_name: The name of the application security group.
    :type application_security_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_security_groups_get(request: web.Request, resource_group_name, application_security_group_name, api_version, subscription_id) -> web.Response:
    """application_security_groups_get

    Gets information about the specified application security group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param application_security_group_name: The name of the application security group.
    :type application_security_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_security_groups_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """application_security_groups_list

    Gets all the application security groups in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_security_groups_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """application_security_groups_list_all

    Gets all application security groups in a subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
