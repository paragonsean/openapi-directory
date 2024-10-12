from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rule_interface import TaxDataTaxRuleInterface
from openapi_server.models.tax_tax_rule_repository_v1_save_put_request import TaxTaxRuleRepositoryV1SavePutRequest
from openapi_server import util


async def tax_tax_rule_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """taxRules

    Save TaxRule

    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxRuleRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)


async def tax_tax_rule_repository_v1_save_put(request: web.Request, body=None) -> web.Response:
    """taxRules

    Save TaxRule

    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxRuleRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
