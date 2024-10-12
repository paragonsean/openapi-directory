from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_data_rule_interface import SalesRuleDataRuleInterface
from openapi_server.models.sales_rule_rule_repository_v1_save_post_request import SalesRuleRuleRepositoryV1SavePostRequest
from openapi_server import util


async def sales_rule_rule_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """salesRules

    Save sales rule.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleRuleRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
