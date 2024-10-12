from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.showback_rule import ShowbackRule
from openapi_server.models.showback_rule_list_result import ShowbackRuleListResult
from openapi_server import util


async def showback_rule_create_update_rule(request: web.Request, api_version, billing_account_id, rule_name, showback_rule) -> web.Response:
    """showback_rule_create_update_rule

    Create/Update showback rule for billing account.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param rule_name: Showback rule name
    :type rule_name: str
    :param showback_rule: Showback rule to create or update.
    :type showback_rule: dict | bytes

    """
    showback_rule = ShowbackRule.from_dict(showback_rule)
    return web.Response(status=200)


async def showback_rule_get_billing_account_id(request: web.Request, api_version, billing_account_id, rule_name) -> web.Response:
    """showback_rule_get_billing_account_id

    Gets the showback rule by rule name.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str
    :param rule_name: Showback rule name
    :type rule_name: str

    """
    return web.Response(status=200)


async def showback_rules_list(request: web.Request, api_version, billing_account_id) -> web.Response:
    """showback_rules_list

    Get list all Showback Rules.

    :param api_version: Version of the API to be used with the client request. The current version is 2019-03-01-preview
    :type api_version: str
    :param billing_account_id: BillingAccount ID
    :type billing_account_id: str

    """
    return web.Response(status=200)
