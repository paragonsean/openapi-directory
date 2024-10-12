from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_coupon_management_v1_generate_post_request import SalesRuleCouponManagementV1GeneratePostRequest
from openapi_server import util


async def sales_rule_coupon_management_v1_generate_post(request: web.Request, body=None) -> web.Response:
    """coupons/generate

    Generate coupon for a rule

    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleCouponManagementV1GeneratePostRequest.from_dict(body)
    return web.Response(status=200)
