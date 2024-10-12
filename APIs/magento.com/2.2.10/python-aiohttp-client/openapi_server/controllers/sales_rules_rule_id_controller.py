from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_data_rule_interface import SalesRuleDataRuleInterface
from openapi_server.models.sales_rule_rule_repository_v1_save_post_request import SalesRuleRuleRepositoryV1SavePostRequest
from openapi_server import util


async def sales_rule_rule_repository_v1_delete_by_id_delete(request: web.Request, rule_id) -> web.Response:
    """salesRules/{ruleId}

    Delete rule by ID.

    :param rule_id: 
    :type rule_id: int

    """
    return web.Response(status=200)


async def sales_rule_rule_repository_v1_get_by_id_get(request: web.Request, rule_id) -> web.Response:
    """salesRules/{ruleId}

    Get rule by ID.

    :param rule_id: 
    :type rule_id: int

    """
    return web.Response(status=200)


async def sales_rule_rule_repository_v1_save_put(request: web.Request, rule_id, body=None) -> web.Response:
    """salesRules/{ruleId}

    Save sales rule.

    :param rule_id: 
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleRuleRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
