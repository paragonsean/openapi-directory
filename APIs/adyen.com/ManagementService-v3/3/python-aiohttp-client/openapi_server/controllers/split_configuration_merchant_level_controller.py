from typing import List, Dict
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.split_configuration import SplitConfiguration
from openapi_server.models.split_configuration_list import SplitConfigurationList
from openapi_server.models.split_configuration_rule import SplitConfigurationRule
from openapi_server.models.update_split_configuration_logic_request import UpdateSplitConfigurationLogicRequest
from openapi_server.models.update_split_configuration_request import UpdateSplitConfigurationRequest
from openapi_server.models.update_split_configuration_rule_request import UpdateSplitConfigurationRuleRequest
from openapi_server import util


async def delete_merchants_merchant_id_split_configurations_split_configuration_id(request: web.Request, merchant_id, split_configuration_id) -> web.Response:
    """Delete a split configuration

    Deletes the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str

    """
    return web.Response(status=200)


async def delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(request: web.Request, merchant_id, split_configuration_id, rule_id) -> web.Response:
    """Delete a split configuration rule

    Deletes the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str
    :param rule_id: 
    :type rule_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_split_configurations(request: web.Request, merchant_id) -> web.Response:
    """Get a list of split configurations

    Returns the list of split configurations for the merchant account.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def get_merchants_merchant_id_split_configurations_split_configuration_id(request: web.Request, merchant_id, split_configuration_id) -> web.Response:
    """Get a split configuration

    Returns the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str

    """
    return web.Response(status=200)


async def patch_merchants_merchant_id_split_configurations_split_configuration_id(request: web.Request, merchant_id, split_configuration_id, body=None) -> web.Response:
    """Update split configuration description

    Changes the description of the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSplitConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(request: web.Request, merchant_id, split_configuration_id, rule_id, body=None) -> web.Response:
    """Update split conditions

    Changes the conditions of the split configuration rule specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The identifier of the split configuration.
    :type split_configuration_id: str
    :param rule_id: The unique identifier of the split configuration rule.
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSplitConfigurationRuleRequest.from_dict(body)
    return web.Response(status=200)


async def patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_split_logic_split_logic_id(request: web.Request, merchant_id, split_configuration_id, rule_id, split_logic_id, body=None) -> web.Response:
    """Update the split logic

    Changes the split logic specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str
    :param rule_id: The unique identifier of the split configuration rule.
    :type rule_id: str
    :param split_logic_id: The unique identifier of the split configuration split.
    :type split_logic_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSplitConfigurationLogicRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_split_configurations(request: web.Request, merchant_id, body=None) -> web.Response:
    """Create a split configuration

    Creates a split configuration for the merchant account specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SplitConfiguration.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_split_configurations_split_configuration_id(request: web.Request, merchant_id, split_configuration_id, body=None) -> web.Response:
    """Create a rule

    Creates a rule in the split configuration specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API - SplitConfiguration read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str
    :param split_configuration_id: The unique identifier of the split configuration.
    :type split_configuration_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SplitConfigurationRule.from_dict(body)
    return web.Response(status=200)
