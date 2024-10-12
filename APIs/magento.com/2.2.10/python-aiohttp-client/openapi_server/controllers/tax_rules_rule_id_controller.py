from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rule_interface import TaxDataTaxRuleInterface
from openapi_server import util


async def tax_tax_rule_repository_v1_delete_by_id_delete(request: web.Request, rule_id) -> web.Response:
    """taxRules/{ruleId}

    Delete TaxRule

    :param rule_id: 
    :type rule_id: int

    """
    return web.Response(status=200)


async def tax_tax_rule_repository_v1_get_get(request: web.Request, rule_id) -> web.Response:
    """taxRules/{ruleId}

    Get TaxRule

    :param rule_id: 
    :type rule_id: int

    """
    return web.Response(status=200)
