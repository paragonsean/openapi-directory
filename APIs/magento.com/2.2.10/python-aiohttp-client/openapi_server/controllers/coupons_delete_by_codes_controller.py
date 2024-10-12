from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_coupon_management_v1_delete_by_codes_post_request import SalesRuleCouponManagementV1DeleteByCodesPostRequest
from openapi_server.models.sales_rule_data_coupon_mass_delete_result_interface import SalesRuleDataCouponMassDeleteResultInterface
from openapi_server import util


async def sales_rule_coupon_management_v1_delete_by_codes_post(request: web.Request, body=None) -> web.Response:
    """coupons/deleteByCodes

    Delete coupon by coupon codes.

    :param body: 
    :type body: dict | bytes

    """
    body = SalesRuleCouponManagementV1DeleteByCodesPostRequest.from_dict(body)
    return web.Response(status=200)
