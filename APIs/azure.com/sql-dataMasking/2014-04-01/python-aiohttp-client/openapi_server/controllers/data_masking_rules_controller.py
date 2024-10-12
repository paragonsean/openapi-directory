from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_masking_rule import DataMaskingRule
from openapi_server.models.data_masking_rule_list_result import DataMaskingRuleListResult
from openapi_server import util


async def data_masking_rules_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, data_masking_policy_name, data_masking_rule_name, parameters) -> web.Response:
    """data_masking_rules_create_or_update

    Creates or updates a database data masking rule.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param data_masking_policy_name: The name of the database for which the data masking rule applies.
    :type data_masking_policy_name: str
    :param data_masking_rule_name: The name of the data masking rule.
    :type data_masking_rule_name: str
    :param parameters: The required parameters for creating or updating a data masking rule.
    :type parameters: dict | bytes

    """
    parameters = DataMaskingRule.from_dict(parameters)
    return web.Response(status=200)


async def data_masking_rules_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, data_masking_policy_name) -> web.Response:
    """data_masking_rules_list_by_database

    Gets a list of database data masking rules.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param data_masking_policy_name: The name of the database for which the data masking rule applies.
    :type data_masking_policy_name: str

    """
    return web.Response(status=200)
