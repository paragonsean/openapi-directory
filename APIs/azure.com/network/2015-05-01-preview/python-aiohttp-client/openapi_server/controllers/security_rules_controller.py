from typing import List, Dict
from aiohttp import web

from openapi_server.models.security_rule import SecurityRule
from openapi_server.models.security_rule_list_result import SecurityRuleListResult
from openapi_server import util


async def security_rules_create_or_update(request: web.Request, resource_group_name, network_security_group_name, security_rule_name, api_version, subscription_id, security_rule_parameters) -> web.Response:
    """security_rules_create_or_update

    The Put network security rule operation creates/updates a security rule in the specified network security group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param security_rule_name: The name of the security rule.
    :type security_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param security_rule_parameters: Parameters supplied to the create/update network security rule operation
    :type security_rule_parameters: dict | bytes

    """
    security_rule_parameters = SecurityRule.from_dict(security_rule_parameters)
    return web.Response(status=200)


async def security_rules_delete(request: web.Request, resource_group_name, network_security_group_name, security_rule_name, api_version, subscription_id) -> web.Response:
    """security_rules_delete

    The delete network security rule operation deletes the specified network security rule.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param security_rule_name: The name of the security rule.
    :type security_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def security_rules_get(request: web.Request, resource_group_name, network_security_group_name, security_rule_name, api_version, subscription_id) -> web.Response:
    """security_rules_get

    The Get NetworkSecurityRule operation retrieves information about the specified network security rule.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param network_security_group_name: The name of the network security group.
    :type network_security_group_name: str
    :param security_rule_name: The name of the security rule.
    :type security_rule_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def security_rules_list(request: web.Request, resource_group_name, network_security_group_name, api_version, subscription_id) -> web.Response:
    """security_rules_list

    The List network security rule operation retrieves all the security rules in a network security group.

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
