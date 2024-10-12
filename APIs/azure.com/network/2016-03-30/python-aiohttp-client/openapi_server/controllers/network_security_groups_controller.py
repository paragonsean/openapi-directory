from typing import List, Dict
from aiohttp import web

from openapi_server.models.network_security_group import NetworkSecurityGroup
from openapi_server.models.network_security_group_list_result import NetworkSecurityGroupListResult
from openapi_server import util


async def network_security_groups_create_or_update(request: web.Request, resource_group_name, network_security_group_name, api_version, subscription_id, parameters) -> web.Response:
    """network_security_groups_create_or_update

    The Put NetworkSecurityGroup operation creates/updates a network security group in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update Network Security Group operation
    :type parameters: dict | bytes

    """
    parameters = NetworkSecurityGroup.from_dict(parameters)
    return web.Response(status=200)


async def network_security_groups_delete(request: web.Request, resource_group_name, network_security_group_name, api_version, subscription_id) -> web.Response:
    """network_security_groups_delete

    The Delete NetworkSecurityGroup operation deletes the specified network security group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_security_groups_get(request: web.Request, resource_group_name, network_security_group_name, api_version, subscription_id, expand=None) -> web.Response:
    """network_security_groups_get

    The Get NetworkSecurityGroups operation retrieves information about the specified network security group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: expand references resources.
    :type expand: str

    """
    return web.Response(status=200)


async def network_security_groups_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """network_security_groups_list

    The list NetworkSecurityGroups returns all network security groups in a resource group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def network_security_groups_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """network_security_groups_list_all

    The list NetworkSecurityGroups returns all network security groups in a subscription

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
