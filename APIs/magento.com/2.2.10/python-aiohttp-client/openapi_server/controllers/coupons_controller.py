from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_coupon_repository_v1_save_post_request import SalesRuleCouponRepositoryV1SavePostRequest
from openapi_server.models.sales_rule_data_coupon_interface import SalesRuleDataCouponInterface
from openapi_server import util


async def sales_rule_coupon_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """coupons

    Save a coupon.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleCouponRepositoryV1SavePostRequest.from_dict(body)
    return web.Response(status=200)
